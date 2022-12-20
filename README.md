# DMDF V2 is Here! For more info, checkout our new whitepaper here

TLDR:
The official GitHub for the Deep Media Data Files, the largest and most diverse public resource for deepfake detection

DMDF_Faces_V2 is a collection of deepfake detection datasets intended to provide you with a ready to use toolkit for deepfake detection. DMDF contains thousands of crops of  real and deepfaked videos.

What's new in V2? We are grateful for the hugely positive response to V1, and we hear your feedback loud and clear. Firstly, DMDF V2 is significantly smaller in download size, making it a much more easily accessible and downloadable tool for deepfake detection. Secondarily, despite the decreased overall size, we have added dramatically more data to DMDF V2. DMDF V2 now contains over 50,000 pre-processed images, split almost exactly between original and manipulated videos. Lastly, we have begun doing demographic analysis of the large quantity of data we are providing, allowing users to more directly understand the racial, emotional, gender, and age distribution of the data they are using.

To download the full DMDF_Faces_V2 datasets use the command:

aws s3 sync s3://dmdf-v2 . --request-payer --region=us-east-1

When you download DMDF_Faces_V2 you will receive a directory pre-structured to accommodate a deepfake detector. The folder is subdivided into test, train, and validations sets, as well as fake and real within each set. Within each fake and real directory, the data is further subdivided into its original dataset. To set up a deepfake detector,  point the data loader to the fake and real data, and the individual crops are already pre-processed. 

The dataset size is 350 GB(Compared to 2.7 TB for V1), and you must be authenticated with your Amazon Web Service account. By setting your region to US-east-1 you can avoid download costs, otherwise it is $0.02 USD/GB, or about $55 for the whole dataset. If you are in academia, or find this cost prohibitive, and are unable to set your region to US-east-1, we would be more than happy to subsidize your download. For more information please reach out to ryan@deepmedia.ai.

For more information, please see the [white paper](https://github.com/deepmediaAI/DMDF/blob/main/DeepMedia%20DMDF_Faces_V1%20%20White%20Paper.pdf) contained in this repository.
