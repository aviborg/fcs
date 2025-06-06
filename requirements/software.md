# Software Requirements Specification (SRS)

## REQ-001: Setpoint Rate Limiting
**Description:** The controller shall limit the rate of change of the setpoint to 5 deg/s.  
**Type:** Functional  
**Verification:** Test Case TC-001  
**Derived From:** SYS-007  
**Allocated To:** FCS_Controller/SetpointLimiter

## REQ-002: Signal Saturation
**Description:** The controller shall clamp actuator commands between -1.0 and 1.0.  
**Type:** Functional  
**Verification:** Test Case TC-002  
**Derived From:** SYS-008  
**Allocated To:** FCS_Controller/Saturation
