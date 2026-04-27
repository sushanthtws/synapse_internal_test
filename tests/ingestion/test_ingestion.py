from app.ingestion.ingestion_pipeline import IngestionPipeline


pipeline = IngestionPipeline()

result = pipeline.run("data/skills")

print(result)