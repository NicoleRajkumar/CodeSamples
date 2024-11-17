// Create an AssetBundle for Windows.
using UnityEngine;
using UnityEditor;

using System.IO;

public class BuildAssetBundles
{

    static void BuildABs()
    {
        string base_dir = "C:/Users/Nicole/Documents/";
        setAssetBundle(base_dir);
        // Put the bundles in a folder called "output"
        string ab_dest = base_dir + "GluMobile/output";
        BuildPipeline.BuildAssetBundles(ab_dest, BuildAssetBundleOptions.None, BuildTarget.StandaloneWindows64);

        AssetDatabase.Refresh();

    }


    static void setAssetBundle(string base_dir)
    {
        
        string folderName = base_dir + "GluMobile/GluMobileUnityProject/Assets/Images";
        string project_dir = base_dir + "GluMobile/GluMobileUnityProject/";

        string[] filePaths = Directory.GetFiles(folderName);
        foreach (string filename in filePaths)
        {
            if(!filename.Contains(".meta")){
                string filename2 = filename.Replace("\\", "/");
                filename2 = filename2.Replace(project_dir, "");
                string[] splitfilename = filename2.Split('/');
                string assetname = splitfilename[splitfilename.Length-1];
                string[] assetnames = assetname.Split('.');
                assetname = assetnames[0];
                AssetImporter AI = AssetImporter.GetAtPath(filename2);
                AI.assetBundleName = assetname;
                AssetDatabase.Refresh();
            }
            
        }
    }
}