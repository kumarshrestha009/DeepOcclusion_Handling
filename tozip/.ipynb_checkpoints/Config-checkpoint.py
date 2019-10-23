#Technical configs

n_threads = 7
verbose = True

#Global configurations
img_index_list = range(2000,3000,10) #images to use
H_grid, W_grid = 80,80

# Config about CRF Inference
parts_root_folder = './Potentials/Parts/Run_transfer/'
#unaries_path = './Potentials/Unaries/Run/%08d.npy'
unaries_path = './Potentials/Unaries/RunFeatures_transfer/%08d.npy'
unaries_path_features = './Potentials/Unaries/RunFeatures_transfer/feat%08d.npy'

n_parts = 9 #Number of classes of classifier. Including foreground class which is the last one

pom_file_path ='./tozip/rectangles80x80.pom'
resize_pom = 4 #Difference in ratio between dimensions for POM file and images saved (4 when images come from VGG)

# Config about POM
Sigma_factor = 3
resize_pom = 4#Difference in ratio between dimensions for POM file and images saved (4 when images come from VGG)

EM_As = [0.0,0.0,0.8,1.4,1.6,1.6,1.6,1.6,1.6]
EM_Ablacks = [2.0,2.0,1.2,0.6,0.4,0.4,0.4,0.4,0.4]
EM_POM_prior = 10

exclusion_rad = 4


# Config about 
bkg_path = './bkg/c%d/%d.png'

#Folder to save POM estimates
POM_out_folder = './POMOutput/transfer/'
#Folder to save Z samples
Z_sample_folder = './ZSamples/'
#Folder to save labels for CNN
labels_folder = './Labels/EM%d/'

#Folder to save test_image
img_logs = './VGG/img_logs/'

#About RGB images

img_path = './tozip/img'

#List of camera names
rgb_name_list = []
cameras_list = range(4)
rgb_name_list.append(img_path+'/C0/%08d.jpg')
rgb_name_list.append(img_path+'/C1/%08d.jpg')
rgb_name_list.append(img_path+'/C2/%08d.jpg')
rgb_name_list.append(img_path+'/C3/%08d.jpg')

rgb_name_list = rgb_name_list[0:len(cameras_list)]

#About CNN
CNN_factor = 4
n_epochs = 80
logs_path = 'VGG/logs/'
net_params_path = 'VGG/models/'
data_augmentation_proportions = [1,2,2,2,4,4,4,4]
BGrate = 5e-4
Regrate = 5e-4
use_bg_pretrained = False

#Val configurations
val_index_list = range(1,500,45) #images to use for validation
GS_out = './Results/validation/GridSearch/Transfer/' #where to store validation dat files
GS_num_iter = 150 #Number of iterations in validation

do_GS_validation = False #Do grid search for validation

#Parameters for POM that we test
GS_As = [0,1,1.3,1.5,1.7,2.0] 
GS_Ps = [0.5,1,2,5,10,15,20] 
GS_Ablacks = [0,0.4,0.8,1.5,2.0,3.0]

