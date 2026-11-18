import os

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'DATA')

for split, sub, txt in [('Train', 'train', 'train.txt'), ('Test', 'test', 'test.txt')]:
    folder = os.path.join(root, split, sub)
    names = sorted(f for f in os.listdir(folder) if f.lower().endswith('.png'))
    with open(os.path.join(root, split, txt), 'w') as f:
        f.write('\n'.join(names) + '\n')
    print(split, len(names), 'images')