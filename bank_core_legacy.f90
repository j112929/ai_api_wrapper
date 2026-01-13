! ************************************************************
! 程序名称: BANK_CORE_LEGACY
! 描述: 模拟 20 年前的银行核心利息计算引擎
! 语言: Fortran 90
! ************************************************************

MODULE INTEREST_ENGINE
    IMPLICIT NONE
    CONTAINS

    ! 核心计算子例程
    ! @param principal: 贷款本金
    ! @param rate: 年利率 (例如 5.0 代表 5%)
    ! @param term: 贷款期限 (月)
    ! @param res: 输出结果 (利息)
    SUBROUTINE CALC_INTEREST(PRINCIPAL, RATE, TERM, RES)
        REAL, INTENT(IN) :: PRINCIPAL
        REAL, INTENT(IN) :: RATE
        REAL, INTENT(IN) :: TERM
        REAL, INTENT(OUT) :: RES
        
        ! 经典利息计算逻辑: I = P * R * T / 12
        ! 注意：旧系统常将利率除以 100
        RES = (PRINCIPAL * (RATE / 100.0) * TERM) / 12.0
    END SUBROUTINE CALC_INTEREST

    ! 辅助函数：计算滞纳金
    FUNCTION GET_PENALTY(AMOUNT) RESULT(PENALTY)
        REAL, INTENT(IN) :: AMOUNT
        REAL :: PENALTY
        ! 模拟滞纳金逻辑：金额的 0.1%
        PENALTY = AMOUNT * 0.001
    END FUNCTION GET_PENALTY

END MODULE INTEREST_ENGINE

! 主程序（仅用于本地测试）
PROGRAM TEST_LEGACY
    USE INTEREST_ENGINE
    REAL :: P, R, T, RESULT
    
    P = 100000.0
    R = 5.0
    T = 12.0
    
    CALL CALC_INTEREST(P, R, T, RESULT)
    PRINT *, "INTEREST RESULT: ", RESULT
END PROGRAM TEST_LEGACY