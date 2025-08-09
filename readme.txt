Why we do Data Ingestion first

Data Ingestion is about getting the raw data into the system and putting it into a safe, ready-to-use format.

It usually:

    Loads data from a source (CSV, SQL, API, etc.).

    Saves the raw version (so we can reproduce results later).

    Splits into train/test datasets — but still raw (no scaling, no encoding yet).

    Stores them for the next stage.

    Splitting early is important — if you transform before splitting, you can accidentally leak information from test to train (data leakage).



    Why Data Transformation is separate

Data Transformation is about preparing the data for ML algorithms.

It usually:

    Loads the raw train/test splits from ingestion.

    Fits preprocessing steps (like scaling, encoding) on train only.

    Applies the same transformations to both train and test.

    Saves the preprocessing object (so we can use it later during prediction