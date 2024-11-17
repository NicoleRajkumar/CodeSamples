Name: Nicole Rajkumar

TECHNOLOGY REQUIREMENTS:

 * Unity 2019.4.18 f1
 * Python 3.9.1
 * External Python Libraries including: (installed in the command line using "python -m pip install")
 	* watchdog(dependancies include : PyYAML, argh, argparse, and pathtools)
 	* PIL(pillow)

SETUP REQUIREMENTS:

 * in GluMobile/pipelineProcess.py,
	* Line 121, the base directory is needed where folder gluMobile is in
	* Line 35, the location of Unity.exe is needed for calling the the C# script in batch mode

 * in GluMobile/GluMobileUnityProject/Assets/Editor/AssetBundleBuilder.cs,
	* Line 12, the base directory is needed where folder gluMobile is in

 *pipelineProcess.py is opened with Python 3.9.1
