# /src/application/use_cases/generate_insights_use_case.py


from src.application.dto.activity_insights_dtos import (
    ActivityInsightsDTO,
)

from src.application.dto.insights_uc_dtos import (
    GenerateInsightsRequestDTO,
    GenerateInsightsResultDTO,
)

from src.application.ports.insights_use_case_ports import (
    ActivityInsightsGeneratorPort,
)



class GenerateInsightsUseCase:
    def __init__(
            self,
            insights_generator: ActivityInsightsGeneratorPort,
    ) -> None:
        self._insights_generator = insights_generator

    def execute(
            self,
            request: GenerateInsightsRequestDTO,
    ) -> GenerateInsightsResultDTO:
        insights: ActivityInsightsDTO = self._insights_generator.generate(
            sensor_ids=request.sensor_ids,
            sensor_profiles=request.sensor_profiles,
            analysis_results=request.analyze_activity_result,
        )

        return GenerateInsightsResultDTO(
            insights=insights,
        )
