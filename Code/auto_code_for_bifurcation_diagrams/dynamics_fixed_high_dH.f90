!---------------------------------------------------------------------- 
!---------------------------------------------------------------------- 
!   spatial_IGP: the spatial IGP model
!---------------------------------------------------------------------- 
!---------------------------------------------------------------------- 

      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP) 
!     ---------- ---- 


! Evaluates the algebraic equations or ODE right hand side

! Input arguments :
!      NDIM   :   Dimension of the ODE system 
!      U      :   State variables
!      ICP    :   Array indicating the free parameter(s)
!      PAR    :   Equation parameters

! Values to be returned :
!      F      :   ODE right hand side values

! Normally unused Jacobian arguments : IJAC, DFDU, DFDP (see manual)


        IMPLICIT NONE
        INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
        DOUBLE PRECISION, INTENT(IN) :: U(NDIM), PAR(*)
        DOUBLE PRECISION, INTENT(OUT) :: F(NDIM)
        DOUBLE PRECISION, INTENT(INOUT) :: DFDU(NDIM,NDIM), DFDP(NDIM,*)

        DOUBLE PRECISION R1,R2,H1,H2,P1,P2  !state variables

        DOUBLE PRECISION g,K            !resource growth parameters - positive
        DOUBLE PRECISION aRH,aRP,aHP    !predation rates - positive
        DOUBLE PRECISION hRH,hRP,hHP    !handling times - positive
        DOUBLE PRECISION eRH,eRP,eHP    !conversion efficiencies - 0=<x=<1
        DOUBLE PRECISION mH,mP          !consumer mortality rates - positive
        DOUBLE PRECISION dR,dH,dP       !dispersal rates - positive

		INTEGER I,J

        !NOTE:  For this code, I've used R to denote the basal resource, 
        !H to denote the intermediate consumer (the herbivore) and P to denote
        !the top consumer, the predator. The indices 1 and 2 are to indicate 
        !which patch each is in. This is a change in notation from the original 
        !formulation, where we used P to indicate the intermediate, and C to 
        !indicate the top, or consumer. I've changed this because 'consumer' 
        !is confusing, since both top and intermediate trophic levels are 
        !'consumers'.  
        R1=U(1)                                         
        R2=U(2)
        H1=U(3)
        H2=U(4)
        P1=U(5)
        P2=U(6) 
        
        !This model is (delibrately) over-parameterized, in that for most 
        !simulations, several of these values will be set at their boundary 
        !conditions; However, AUTO should be able to deal with this,
        !and it will make future sensitivity tests simpler. 
        g=PAR(1)
        K=PAR(2)
        aRH=PAR(3)
        aRP=PAR(4)
        aHP=PAR(5)
        hRH=PAR(6)
        hRP=PAR(7)
        hHP=PAR(8)
        eRH=PAR(9)
        eRP=PAR(10)
        !NOTE: PAR(11) is skipped, because AUTO reserves this
        !parameter exclusively for the system period
        eHP=PAR(12)     
        mH=PAR(13)
        mP=PAR(14)
        dR=PAR(15)
        dH=PAR(16)
        dP=PAR(17)



        !This model assumes: 
        !Logistic growth for the resource;
        !Type II Holling-Disc func responses for both trophic levels (which 
        !includes the Type I func response as a boundary case, as the handling 
        !time goes to zero). Also note that, for the top consumer, its 
        !predation rate on each underlying trophic level depends on the other, 
        !since we assume that time spent handling one species takes away from 
        !the time available to hunt the other species; 
        !The two consumers suffer from density-independent per-capita mortality;
        !All three levels have density-independent per-capita dispersal. 
        !       
        F(1)=g*R1*(1-R1/K)-aRH*R1*H1/(1+aRH*hRH*R1)-aRP*R1*P1/(1+aRP*hRP*R1+aHP*hHP*H1)+dR*(R2-R1)
        F(2)=g*R2*(1-R2/K)-aRH*R2*H2/(1+aRH*hRH*R2)-aRP*R2*P2/(1+aRP*hRP*R2+aHP*hHP*H2)+dR*(R1-R2)
        F(3)=eRH*aRH*R1*H1/(1+aRH*hRH*R1)-aHP*H1*P1/(1+aRP*hRP*R1+aHP*hHP*H1)-mH*H1+dH*(H2-H1)
        F(4)=eRH*aRH*R2*H2/(1+aRH*hRH*R2)-aHP*H2*P2/(1+aRP*hRP*R2+aHP*hHP*H2)-mH*H2+dH*(H1-H2)
        F(5)=(eRP*aRP*R1+eHP*aHP*H1)*P1/(1+aRP*hRP*R1+aHP*hHP*H1)-mP*P1+dP*(P2-P1)
        F(6)=(eRP*aRP*R2+eHP*aHP*H2)*P2/(1+aRP*hRP*R2+aHP*hHP*H2)-mP*P2+dP*(P1-P2)



      IF(IJAC.EQ.0)RETURN
      !This calculates the Jacobian matrix for this system
        DO I=1,6
         DO J=1,6
          DFDU(I,J)=0.d0
         ENDDO
        ENDDO
	!Jacobian calcuated using Matlab's symbolic algebra toolbox. 
        !NOTE: for each entry of the Jacobian (i,j), the value is dx_i/dp_j
        DFDU(1,1)=(H1*R1*aRH**2*hRH)/(R1*aRH*hRH + 1)**2 - g*(R1/K - 1) - (H1*aRH)/(R1*aRH*hRH + 1) 
	  DFDU(1,1) = DFDU(1,1) - (P1*aRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - (R1*g)/K - dR 
	  DFDU(1,1) = DFDU(1,1) + (P1*R1*aRP**2*hRP)/(H1*aHP*hHP+R1*aRP*hRP + 1)**2
        DFDU(1,3) = (P1*R1*aHP*aRP*hHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)**2 - (R1*aRH)/(R1*aRH*hRH + 1)
        DFDU(1,5) = -(R1*aRP)/(H1*aHP*hHP + R1*aRP*hRP + 1)

        DFDU(2,2)=(H2*R2*aRH**2*hRH)/(R2*aRH*hRH + 1)**2 - g*(R2/K - 1) - (H2*aRH)/(R2*aRH*hRH + 1) 
	  DFDU(2,2) = DFDU(2,2) - (P2*aRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - (R2*g)/K - dR 
	  DFDU(2,2) = DFDU(2,2) + (P2*R2*aRP**2*hRP)/(H2*aHP*hHP+R2*aRP*hRP + 1)**2
        DFDU(2,4) = (P2*R2*aHP*aRP*hHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)**2 - (R2*aRH)/(R2*aRH*hRH + 1)
        DFDU(2,6) = -(R2*aRP)/(H2*aHP*hHP + R2*aRP*hRP + 1)


        DFDU(3,1) = (H1*aRH*eRH)/(R1*aRH*hRH + 1) - (H1*R1*aRH**2*eRH*hRH)/(R1*aRH*hRH + 1)**2 
          DFDU(3,1) = DFDU(3,1) + (H1*P1*aHP*aRP*hRP)/(H1*aHP*hHP + R1*aRP*hRP + 1)**2
        DFDU(3,3) = (R1*aRH*eRH)/(R1*aRH*hRH + 1) - mH - (P1*aHP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - dH 
	  DFDU(3,3) = DFDU(3,3) + (H1*P1*aHP**2*hHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)**2
        DFDU(3,5) = -(H1*aHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)

        DFDU(4,2) = (H2*aRH*eRH)/(R2*aRH*hRH + 1) - (H2*R2*aRH**2*eRH*hRH)/(R2*aRH*hRH + 1)**2 
          DFDU(4,2) = DFDU(4,2) + (H2*P2*aHP*aRP*hRP)/(H2*aHP*hHP + R2*aRP*hRP + 1)**2
        DFDU(4,4) = (R2*aRH*eRH)/(R2*aRH*hRH + 1) - mH - (P2*aHP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - dH 
	  DFDU(4,4) = DFDU(4,4) + (H2*P2*aHP**2*hHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)**2
        DFDU(4,6) = -(H2*aHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)



        DFDU(5,1) = (P1*aRP*eRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) 
	  DFDU(5,1) = DFDU(5,1) - (P1*aRP*hRP*(H1*aHP*eHP + R1*aRP*eRP))/(H1*aHP*hHP + R1*aRP*hRP + 1)**2
        DFDU(5,3) = (P1*aHP*eHP)/(H1*aHP*hHP + R1*aRP*hRP + 1) 
	  DFDU(5,3) = DFDU(5,3) - (P1*aHP*hHP*(H1*aHP*eHP + R1*aRP*eRP))/(H1*aHP*hHP + R1*aRP*hRP + 1)**2
        DFDU(5,5) = (H1*aHP*eHP + R1*aRP*eRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - mP - dP




        DFDU(6,2) = (P2*aRP*eRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) 
	  DFDU(6,2) = DFDU(6,2) - (P2*aRP*hRP*(H2*aHP*eHP + R2*aRP*eRP))/(H2*aHP*hHP + R2*aRP*hRP + 1)**2
        DFDU(6,4) = (P2*aHP*eHP)/(H2*aHP*hHP + R2*aRP*hRP + 1) 
	  DFDU(6,4) = DFDU(6,4) - (P2*aHP*hHP*(H2*aHP*eHP + R2*aRP*eRP))/(H2*aHP*hHP + R2*aRP*hRP + 1)**2
        DFDU(6,6) = (H2*aHP*eHP + R2*aRP*eRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - mP - dP


	DFDU(1,2) = dR
	DFDU(3,4) = dH
	DFDU(5,6) = dP

        DFDU(2,1) = dR
        DFDU(4,3) = dH
	DFDU(6,5) = dP




      IF(IJAC.EQ.1)RETURN
        DO I=1,6
         DO J=1,17
          DFDP(I,J)=0.d0
          ENDDO
       ENDDO    

      
  
      DFDP(1,15) = R2 - R1
      DFDP(3,16) = H2 - H1
      DFDP(5,17) = P2 - P1

      DFDP(1,2) = (R1**2*g)/K**2
      DFDP(2,2) = (R2**2*g)/K**2

      DFDP(2,15) = R1 - R2
      DFDP(4,16) = H1 - H2
      DFDP(6,17) = P1 - P2
        

      END SUBROUTINE FUNC
!---------------------------------------------------------------------- 

      SUBROUTINE STPNT(NDIM,U,PAR,T) 
!     ---------- ----- 
! Specifies the initial parameter values and state values. 

        IMPLICIT NONE
        INTEGER, INTENT(IN) :: NDIM
        DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM),PAR(*)
        DOUBLE PRECISION, INTENT(IN) :: T
        par(1)=1.      	!g
        par(2)=0.5253  	!K
        par(3)= 0.1    	!aRH
        par(4)=0.    	!aRP
        par(5)=0.1    	!aHP
        par(6)=0.      	!hRH
        par(7)=10.     	!hRP
        par(8)=10.	!hHP
        par(9)=1.       !eRH
        par(10)=1.      !eRP	
        par(12)=1.      !eHP
        par(13)=0.04   	!mH
        par(14)=0.08   	!mP
        par(15)=5 	!dR
        par(16)=0.1     !dH
        par(17)=0.1	!dP


        U(1)=par(2)
        U(2)=par(2)
        U(3)=0
        U(4)=0
        U(5)=0
        U(6)=0
        


      END SUBROUTINE STPNT
!---------------------------------------------------------------------- 

      SUBROUTINE BCND 
      END SUBROUTINE BCND

      SUBROUTINE ICND 
      END SUBROUTINE ICND

      SUBROUTINE FOPT 
      END SUBROUTINE FOPT

      SUBROUTINE PVLS
      END SUBROUTINE PVLS
