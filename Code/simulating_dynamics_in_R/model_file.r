#require(deSolve)
#File specifying the overall dynamics for the equations. Required to run sims
TriTrophDynamics = function(t,y, parms,IGP=FALSE, conversion_costs=FALSE){
  if(!IGP){
    aRP = 0; hRP =0; eRP = 1
  }
  if(!conversion_costs){
    eRP = 1; eRH = 1; eHP = 1
  }
  
  with(as.list(c(y,parms)),{
  #R1=y$R1; R2=y$R2; H1=y$H1; H2=y$H2;P1=y$P1;P2=y$P2
  f_RH1 = aRH*R1*H1/(1+aRH*hRH*R1)
  f_RH2 = aRH*R2*H2/(1+aRH*hRH*R2)
  f_RP1 = aRP*R1*P1/(1+aRP*hRP*R1+aHP*hHP*H1)
  f_RP2 = aRP*R2*P2/(1+aRP*hRP*R2+aHP*hHP*H2)
  f_HP1 = aHP*H1*P1/(1+aRP*hRP*R1+aHP*hHP*H1)
  f_HP2 = aHP*H2*P2/(1+aRP*hRP*R2+aHP*hHP*H2)
  
  R1_out=g*R1*(1-R1/K)-f_RH1-f_RP1+dR*(R2-R1)
  R2_out=g*R2*(1-R2/K)-f_RH2-f_RP2+dR*(R1-R2)
  
  H1_out=eRH*f_RH1-f_HP1-mH*H1+dH*(H2-H1)
  H2_out=eRH*f_RH2-f_HP2-mH*H2+dH*(H1-H2)
  
  P1_out=eRP*f_RP1 + eHP*f_HP1 - mP*P1+dP*(P2-P1) 
  P2_out=eRP*f_RP2 + eHP*f_HP2 - mP*P2+dP*(P1-P2) 
  
  

  out_vector = c(R1=R1_out, R2= R2_out, 
                 H1=H1_out, H2=H2_out,
                 P1=P1_out,P2=P2_out)
  return(list(out_vector))
  }
  )
}

TriTrophJacob = function(t,y, parms,IGP=FALSE, conversion_costs=FALSE){
  if(!IGP){
    aRP = 0; hRP =0; eRP = 1
  }
  if(!conversion_costs){
    eRP = 1; eRH = 1; eHP = 1
  }
  with(as.list(c(y,parms)),{
    DFDU = matrix(rep(0, times= 36), nrow=6)
    DFDU[1,1]=(H1*R1*aRH^2*hRH)/(R1*aRH*hRH + 1)^2 - g*(R1/K - 1) - (H1*aRH)/(R1*aRH*hRH + 1) 
    DFDU[1,1] = DFDU[1,1] - (P1*aRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - (R1*g)/K - dR 
    DFDU[1,1] = DFDU[1,1] + (P1*R1*aRP^2*hRP)/(H1*aHP*hHP+R1*aRP*hRP + 1)^2
    DFDU[1,3] = (P1*R1*aHP*aRP*hHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)^2 - (R1*aRH)/(R1*aRH*hRH + 1)
    DFDU[1,5] = -(R1*aRP)/(H1*aHP*hHP + R1*aRP*hRP + 1)
    
    DFDU[2,2]=(H2*R2*aRH^2*hRH)/(R2*aRH*hRH + 1)^2 - g*(R2/K - 1) - (H2*aRH)/(R2*aRH*hRH + 1) 
    DFDU[2,2] = DFDU[2,2] - (P2*aRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - (R2*g)/K - dR 
    DFDU[2,2] = DFDU[2,2] + (P2*R2*aRP^2*hRP)/(H2*aHP*hHP+R2*aRP*hRP + 1)^2
    DFDU[2,4] = (P2*R2*aHP*aRP*hHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)^2 - (R2*aRH)/(R2*aRH*hRH + 1)
    DFDU[2,6] = -(R2*aRP)/(H2*aHP*hHP + R2*aRP*hRP + 1)
    
    
    DFDU[3,1] = (H1*aRH*eRH)/(R1*aRH*hRH + 1) - (H1*R1*aRH^2*eRH*hRH)/(R1*aRH*hRH + 1)^2 
    DFDU[3,1] = DFDU[3,1] + (H1*P1*aHP*aRP*hRP)/(H1*aHP*hHP + R1*aRP*hRP + 1)^2
    DFDU[3,3] = (R1*aRH*eRH)/(R1*aRH*hRH + 1) - mH - (P1*aHP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - dH 
    DFDU[3,3] = DFDU[3,3] + (H1*P1*aHP^2*hHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)^2
    DFDU[3,5] = -(H1*aHP)/(H1*aHP*hHP + R1*aRP*hRP + 1)
    
    DFDU[4,2] = (H2*aRH*eRH)/(R2*aRH*hRH + 1) - (H2*R2*aRH^2*eRH*hRH)/(R2*aRH*hRH + 1)^2 
    DFDU[4,2] = DFDU[4,2] + (H2*P2*aHP*aRP*hRP)/(H2*aHP*hHP + R2*aRP*hRP + 1)^2
    DFDU[4,4] = (R2*aRH*eRH)/(R2*aRH*hRH + 1) - mH - (P2*aHP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - dH 
    DFDU[4,4] = DFDU[4,4] + (H2*P2*aHP^2*hHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)^2
    DFDU[4,6] = -(H2*aHP)/(H2*aHP*hHP + R2*aRP*hRP + 1)
    
    
    
    DFDU[5,1] = (P1*aRP*eRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) 
    DFDU[5,1] = DFDU[5,1] - (P1*aRP*hRP*(H1*aHP*eHP + R1*aRP*eRP))/(H1*aHP*hHP + R1*aRP*hRP + 1)^2
    DFDU[5,3] = (P1*aHP*eHP)/(H1*aHP*hHP + R1*aRP*hRP + 1) 
    DFDU[5,3] = DFDU[5,3] - (P1*aHP*hHP*(H1*aHP*eHP + R1*aRP*eRP))/(H1*aHP*hHP + R1*aRP*hRP + 1)^2
    DFDU[5,5] = (H1*aHP*eHP + R1*aRP*eRP)/(H1*aHP*hHP + R1*aRP*hRP + 1) - mP - dP
    
    
    
    
    DFDU[6,2] = (P2*aRP*eRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) 
    DFDU[6,2] = DFDU[6,2] - (P2*aRP*hRP*(H2*aHP*eHP + R2*aRP*eRP))/(H2*aHP*hHP + R2*aRP*hRP + 1)^2
    DFDU[6,4] = (P2*aHP*eHP)/(H2*aHP*hHP + R2*aRP*hRP + 1) 
    DFDU[6,4] = DFDU[6,4] - (P2*aHP*hHP*(H2*aHP*eHP + R2*aRP*eRP))/(H2*aHP*hHP + R2*aRP*hRP + 1)^2
    DFDU[6,6] = (H2*aHP*eHP + R2*aRP*eRP)/(H2*aHP*hHP + R2*aRP*hRP + 1) - mP - dP
    
    
    DFDU[1,2] = dR
    DFDU[3,4] = dH
    DFDU[5,6] = dP
    
    DFDU[2,1] = dR
    DFDU[4,3] = dH
    DFDU[6,5] = dP
    return(DFDU)
  })
}