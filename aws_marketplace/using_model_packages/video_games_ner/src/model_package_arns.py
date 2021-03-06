class ModelPackageArnProvider:

    @staticmethod
    def get_model_package_arn(current_region):
        mapping = {
            "ap-south-1": "arn:aws:sagemaker:ap-south-1:077584701553:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "ap-northeast-2": "arn:aws:sagemaker:ap-northeast-2:745090734665:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "ap-southeast-1": "arn:aws:sagemaker:ap-southeast-1:192199979996:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "ap-southeast-2": "arn:aws:sagemaker:ap-southeast-2:666831318237:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "ap-northeast-1": "arn:aws:sagemaker:ap-northeast-1:977537786026:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "ca-central-1": "arn:aws:sagemaker:ca-central-1:470592106596:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "eu-central-1": "arn:aws:sagemaker:eu-central-1:446921602837:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "eu-west-1": "arn:aws:sagemaker:eu-west-1:985815980388:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "eu-west-2": "arn:aws:sagemaker:eu-west-2:856760150666:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "us-east-1": "arn:aws:sagemaker:us-east-1:865070037744:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "us-east-2": "arn:aws:sagemaker:us-east-2:057799348421:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "us-west-1": "arn:aws:sagemaker:us-west-1:382657785993:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "us-west-2": "arn:aws:sagemaker:us-west-2:594846645681:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "eu-west-3": "arn:aws:sagemaker:eu-west-3:843114510376:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "sa-east-1": "arn:aws:sagemaker:sa-east-1:270155090741:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8",
            "eu-north-1": "arn:aws:sagemaker:eu-north-1:136758871317:model-package/ner-video-games-2020-01-30-21--abf726bda2b3d5f395382b8e7fda0ee8"
        }
        return mapping[current_region]
