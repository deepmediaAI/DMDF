# DMDF TLDR
The official GitHub for the Deep Media Data Files, the largest public resource for deepfake detection

DMDF_Faces_V1 is a collection of deepfake detection datasets intended to provide you with a ready to use toolkit for deepfake detection. DMDF contains thousands of crops of  real and deepfaked videos.

To download the full DMDF_Faces_V1 datasets use the command:

aws s3 sync s3://dmdf-v1 . --request-payer --region=us-east-1

When you download DMDF_Faces_V1 you will receive a directory pre-structured to accommodate a deepfake detector. The folder is subdivided into test, train, and validations sets, as well as fake and real within each set. Within each fake and real directory, the data is further subdivided into its original dataset. To set up a deepfake detector,  point the data loader to the fake and real data, and the individual crops are already pre-processed. 

The dataset size is 2.7 TB, and you must be authenticated with your Amazon Web Service account. By setting your region to US-east-1 you can avoid download costs, otherwise it is $0.02 USD/GB, or about $55 for the whole dataset. If you are in academia, or find this cost prohibitive, and are unable to set your region to US-east-1, we would be more than happy to subsidize your download. For more information please reach out to ryan@deepmedia.ai.

For more information, please see the [white paper](https://github.com/deepmediaAI/DMDF/blob/main/DeepMedia%20DMDF_Faces_V1%20%20White%20Paper.pdf) contained in this repository.
