import yaml
imgs_path = './perfect_result.dat'
idx_ref = './holidays_images.dat'
result = './result.yaml'
with open(imgs_path) as f:
    imgs = [l.strip().split(' ')[0] for l in f.readlines()]
with open(imgs_path) as f:
    gt = [l.strip().split(' ')[0::2] for l in f.readlines()]
with open(idx_ref) as f:
    ref = [l.strip() for l in f.readlines()]

idx_imgs = [ref.index(each) for each in imgs]
idx_gt = []
for ll in gt:
    idx = [ref.index(each) for each in ll]
    idx_gt.append(idx)

res = []
for idx_i, idx_g in zip(idx_imgs, idx_gt):
    entry = {}
    entry['query_id'] = idx_i
    entry['positive_id'] = idx_g
    res.append(entry)

with open(result, 'w') as f:
    yaml.dump(res, f)
'''
for i,(img_idx, gt_idx) in enumerate(zip(idx_imgs,idx_gt)):
    if i > 30:
        break
    print('{}\t{}'.format(img_idx,gt_idx))
for each in imgs[:3]:
    print(each)
for each in idx_imgs[:3]:
    print(each)

for each in gt[:3]:
    print(each)
for each in idx_gt[:3]:
    print(each)


for i, (k,v) in enumerate(res.items()):
    if i>3:
        break
    print('{}\t{}'.format(k,v))
'''