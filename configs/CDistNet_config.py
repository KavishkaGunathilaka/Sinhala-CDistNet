import os


dst_vocab = 'cdistnet/utils/dict_394.txt'   
dst_vocab_size = 394
rgb2gray =False
keep_aspect_ratio = False # Aspect ratio=True does not work
width = 256 #256
height = 32 #32
max_width = 180
is_lower = False 
cnn_num = 2
leakyRelu = False
hidden_units = 512
ff_units = 1024      #ff
scale_embedding = True
attention_dropout_rate = 0.0
residual_dropout_rate = 0.1
num_encoder_blocks = 3
num_decoder_blocks = 3
num_heads = 8
beam_size = 10
n_best = 1
data_aug = False
num_fiducial = 20           #number of fiducial points of TPS-STN
train_method = 'origin'     #dist:  use distributed train method origin
optim = 'origin'

# method choice
tps_block = 'TPS'      # TPS None
feature_block = 'Resnet45'    # Resnet45 Resnet31 MTB

lmdb_train_dir = os.environ.get('TRAIN_LMDB_DIR', 'train-data')
lmdb_test_dir = os.environ.get('TEST_LMDB_DIR', 'test-data')
model_path = os.environ.get('MODEL_PATH')
train_epochs = int(os.environ.get('NUM_TRAIN_EPOCHS', 100))
current_epoch = int(os.environ.get('CURRENT_EPOCH', 0))

train = dict(
    grads_clip=5,
    optimizer='adam_decay',  # not used
    learning_rate_warmup_steps=10000,
    label_smoothing=True,  # fixed in code
    shared_embedding=False,  # not used
    device='cpu',
    gt_file=[lmdb_train_dir],
    num_worker=0,
    # model_dir ='model/test',
    model_dir='models/reconstruct_CDistNet_3_10', 
    num_epochs=train_epochs,
    # gpu_device_ids=[1,2,3,4,5,6,7],
    batch_size=4,  # 4gpu 1800
    model=model_path,
    # model ='models/new_baseline_sem_pos_pos_vis_3_32*128_tps_resnet45_epoch_6/model_epoch_5.pth',
    current_epoch=current_epoch,  # epoch start
    save_iter=10,
    display_iter=10,
    tfboard_iter=1000,
    eval_iter=50,
)


val = dict(
    model='models/baseline_two_32*100_1d_2cnn-test/model_epoch_1.pth',  # abandon
    device='cuda',
    # is_val_gt=True,
    image_dir='datasets/NewVersion/val_data',
    gt_file= [lmdb_test_dir],
    # gt_file=['datasets/NewVersion/val_data/val_data.txt'],
    # gt_file='../dataset/MJ/MJ_valid/',
    batch_size=4,  # 4gpu 1800
    num_worker=0,
)


test = dict(
    test_one=False,
    device='cuda',
    rotate=False,  
    best_acc_test=True,  # test best_acc
    eval_all=False,  # test all model_epoch_9_iter_4080.pth
    s_epoch=7,  # start_epoch
    e_epoch=10,  
    avg_s=-1,  
    avg_e=9,
    avg_all=False,  
    is_test_gt=False,
    image_dir= None,     #if is_test_gt == False,needn't use image_dir
    test_list=[lmdb_test_dir],
    batch_size=4,
    num_worker=0,
    model_dir='/content/Sinhala-CDistNet/models/reconstruct_CDistNet_3_10',  # load test model
    script_path='utils/Evaluation_TextRecog/script.py',
    python_path='/data1/zs/anaconda3/envs/py2/bin/python' #abandon
)
