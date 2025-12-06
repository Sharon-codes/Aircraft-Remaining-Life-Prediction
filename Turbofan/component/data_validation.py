from Turbofan.logger import logging
from Turbofan.exception import TurboException 
from Turbofan.entity.config_entity import DataIngestionConfig, DataValidationConfig 
from Turbofan.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact 
# from evidently.report import Report
# from evidently.metric_preset import DataDriftPreset
import os,sys 
import pandas as pd 
import json 



class DataValidation: 

    def __init__(self , data_validation_config:DataValidationConfig, 
                        data_ingestion_artifact:DataIngestionArtifact) -> None:
        try : 
            logging.info(f"{'=='*20} Data Validatioon Started {'=='*20}")
            self.data_validation_config = data_validation_config 
            self.data_ingestion_artifact = data_ingestion_artifact 

        except Exception as e  :
            raise TurboException(e,sys)

    def get_train_test_df(self): 
        try : 
            logging.info("Getting train test dataframe") 
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df , test_df
        except Exception as e : 
            raise TurboException(e,sys)

    def is_train_test_file_exists(self): 
        try :
            logging.info("Checking training and test file exists or not ")
            is_train_file_path = False 
            is_test_file_path = False 

            train_file_path = self.data_ingestion_artifact.train_file_path 
            test_file_path = self.data_ingestion_artifact.test_file_path 

            is_train_file_path = os.path.exists(train_file_path)
            is_test_file_path = os.path.exists(test_file_path)

            available = is_train_file_path and is_test_file_path 

            if not available : 
                train_file_path = self.data_ingestion_artifact.train_file_path 
                test_file_path = self.data_ingestion_artifact.test_file_path 

                message = f"Training file {train_file_path} or test file {test_file_path} is not present in directory"
                raise Exception(message)
            return available

        except Exception as e : 
            raise TurboException(e,sys)

    def get_and_save_data_drift_report(self): 
        try :
            # Simplified data drift check without evidently
            train_df, test_df = self.get_train_test_df()
            
            # Basic statistical comparison
            drift_report = {
                "train_shape": train_df.shape,
                "test_shape": test_df.shape,
                "train_columns": list(train_df.columns),
                "test_columns": list(test_df.columns),
                "train_stats": train_df.describe().to_dict(),
                "test_stats": test_df.describe().to_dict(),
                "message": "Basic data validation completed (evidently disabled)"
            }

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            with open(report_file_path, "w") as report_file:
                json.dump(drift_report, report_file, indent=6)
            return drift_report 
        except Exception as e : 
            raise TurboException(e, sys)

    def save_data_drift_report_page(self): 
        try : 
            # Simplified HTML report generation without evidently
            train_df, test_df = self.get_train_test_df()
            
            # Create a simple HTML report
            html_content = f"""
            <html>
            <head><title>Data Validation Report</title></head>
            <body>
                <h1>Data Validation Report</h1>
                <h2>Dataset Shapes</h2>
                <p>Train dataset shape: {train_df.shape}</p>
                <p>Test dataset shape: {test_df.shape}</p>
                <h2>Train Dataset Statistics</h2>
                {train_df.describe().to_html()}
                <h2>Test Dataset Statistics</h2>
                {test_df.describe().to_html()}
                <p><em>Note: This is a simplified report (evidently disabled)</em></p>
            </body>
            </html>
            """

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir, exist_ok=True)

            with open(report_page_file_path, "w") as f:
                f.write(html_content)

        except Exception as e : 
            raise TurboException(e, sys)

    def is_data_drift_found(self): 
        try : 
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True 
        except Exception as e : 
            raise TurboException(e,sys)

    def initiate_data_validation(self) -> DataValidationArtifact: 
        try : 
            self.is_train_test_file_exists()
            self.is_data_drift_found()
            data_validation_artifact = DataValidationArtifact( 
                schema_file_path=self.data_validation_config.schema_file_path , 
                report_file_path= self.data_validation_config.report_file_path , 
                report_page_file_path=self.data_validation_config.report_page_file_path ,
                is_validated=True , 
                message = "Data Validation succesfull"
            )
            logging.info(f"Data Validation artifact {data_validation_artifact}")

            return data_validation_artifact
        except Exception as e : 
            raise TurboException(e,sys)


