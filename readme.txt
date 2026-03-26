第一轮
python main.py pig_fight RGB \
    --arch mobilenetv2 \
    --num_segments 8 \
    --gd 20 \
    --lr 0.01 \
    --wd 1e-4 \
    --lr_steps 20 40 \
    --epochs 50 \
    --batch-size 8 \
    -j 16 \
    --dropout 0.5 \
    --consensus_type=avg \
    --eval-freq=1 \
    --shift \
    --shift_div=8 \
    --shift_place=blockres \
    --npb \
    --pretrain=TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth





python test_models.py pig_fight --weights=/home/temporal-shift-module-master/temporal-shift-module-master/checkpoint/007/TSM_pig_fight_RGB_mobilenetv2_shift8_blockres_avg_segment8_e60_TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth/ckpt.best.pth.tar --test_segments=8 --test_crops=1 --batch_size=8 --dense_sample --workers=4 --csv_file=./test_results.csv --is_shift --arch=mobilenetv2







python test_video_improved.py \
    /home/temporal-shift-module-master/temporal-shift-module-master/pig47.mp4 \
     /home/temporal-shift-module-master/temporal-shift-module-master/checkpoint/007/TSM_pig_fight_RGB_mobilenetv2_shift8_blockres_avg_segment8_e60_TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth/ckpt.best.pth.tar \
    --class_names fight nofight \
    --temporal_smooth 5 \
    --confidence_threshold 0.7 \
    --update_interval 4 \







python test_video_improved.py \
    /home/temporal-shift-module-master/temporal-shift-module-master/pig47.mp4 \
/home/temporal-shift-module-master/temporal-shift-module-master/checkpoint/012/TSM_pig_fight_RGB_mobilenetv2_shift8_blockres_avg_segment8_e80_/home/temporal-shift-module-master/temporal-shift-module-master/TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth/ckpt.pth.tar \
    --class_names fight nofight \
    --temporal_smooth 7 \
    --confidence_threshold 0.55 \
    --update_interval 4 \


python main-1.py pig_fight RGB \
    --arch mobilenetv2 \
    --num_segments 8 \
    --gd 20 \
    --lr 0.0008 \
    --weight-decay 8e-4 \
    --lr_steps 15 30 45 \
    --epochs 60 \
    --batch-size 8 \
    -j 16 \
    --dropout 0.65 \
    --consensus_type avg \
    --eval-freq 1 \
    --shift \
    --shift_div 8 \
    --shift_place blockres \
    --npb \
    --pretrain TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth

python main.py pig_fight RGB --arch mobilenetv2 --num_segments 8 --gd 20 \
--lr 0.0001 --weight-decay 8e-4 --lr_steps 20 35 50 --epochs 80 \
--batch-size 8 -j 16 --dropout 0.65 --consensus_type avg --eval-freq 1 \
--shift --shift_div 8 --shift_place blockres --npb \
--resume /home/temporal-shift-module-master/temporal-shift-module-master/checkpoint/007/TSM_pig_fight_RGB_mobilenetv2_shift8_blockres_avg_segment8_e60_TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth/ckpt.best.pth.tar --pretrained /home/temporal-shift-module-master/temporal-shift-module-master/TSM_kinetics_RGB_mobilenetv2_shift8_blockres_avg_segment8_e100_dense.pth


