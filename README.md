# MER_dataset_cleaning
Steps I used to clean the Micro_Expressions dataset

- Downloaded bulk images from google image search using "[Download All Images](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm?hl=en)" Chrome extension
- Removed duplicate images -> [1_removeDuplicate.py](https://github.com/k-m-irfan/MER_dataset_cleaning/blob/main/1_removeDuplicate.py)
- Face detection and face crop (also removes images without face) -> [2_faceCrop.py](https://github.com/k-m-irfan/MER_dataset_cleaning/blob/main/2_faceCrop.py)
- Removed small images < 80x80 pixels and resized the remaining images to 80x80 pixels -> [3_lowRes_remove.py](https://github.com/k-m-irfan/MER_dataset_cleaning/blob/main/3_lowRes_remove.py)
- Renamed images based on their class followed by number -> [4_rename.py](https://github.com/k-m-irfan/MER_dataset_cleaning/blob/main/4_rename.py)
- Manually checked the dataset for any errors.

Dataset: [Micro_Expressions](https://www.kaggle.com/datasets/kmirfan/micro-expressions)

Notebook (kaggle): [micro_expression_classification](https://www.kaggle.com/code/kmirfan/micro-expression-classification)

The trained model gives 78% accuracy on the validation set and 81.4% accuracy on the test set.
