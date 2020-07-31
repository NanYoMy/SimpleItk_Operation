import SimpleITK as sitk
import numpy as np
def convert(path):
    nii_img=sitk.ReadImage(path)
    nii_img=sitk.Cast(nii_img,sitk.sitkLabelUInt16)
    dict={3:1,2:1}
    nii_img=sitk.ChangeLabelLabelMap(nii_img,dict)
    nii_img=sitk.Cast(nii_img,sitk.sitkUInt16)
    sitk.WriteImage(nii_img,path+"_convert.nii.gz")
if __name__=="__main__":
    convert("./mtc.nii.gz")