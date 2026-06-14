# /src/interface_adapters/controllers/analysis_controller.py

from src.application.use_cases.use_cases_interactor import (
    RunAnalysisUseCasesInteractor,
    # AnalyzeMovementPatternsInteractor,
)

from src.application.dto.run_analysis_use_cases_dtos import (
    RunAnalysisUseCasesRequestDTO,
    RunAnalysisUseCasesResultDTO,
)

import logging

logger = logging.getLogger(__name__)


class RunAnalysisUseCasesController:
    def __init__(
            self,
            run_analysis_use_cases: RunAnalysisUseCasesInteractor,
            # analyze_movements_use_case: AnalyzeMovementPatternsInteractor,
    ) -> None:
        self._run_analysis_use_cases = run_analysis_use_cases
        # self._analyze_movements_uc = analyze_movements_use_case

    def run(
            self,
            request: RunAnalysisUseCasesRequestDTO,
    ) -> RunAnalysisUseCasesResultDTO:

        logging.info("Starting orchestration use case...")

        result: RunAnalysisUseCasesResultDTO = (
            self._run_analysis_use_cases.execute(request)
        )

        logging.info("   ... all use case executions complete.")

        return result
