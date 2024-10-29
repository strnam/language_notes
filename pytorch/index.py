# %%
import torch 

# %% How multiple indices can be selected
max_steps = 20
max_slots = 6 # max agents 
img_dim = (16, 15)

img_obs = torch.zeros((max_steps, max_slots, img_dim[0], img_dim[1]))
mask = torch.zeros((max_steps, max_slots))

mask[0, 0] = 1
mask[4, 5] = 1

indices = mask.nonzero()
print("indices shape: ", indices.shape)
print( "img_obs shape: ", img_obs.shape) # 
print("img_obs[indices] shape: ", img_obs[indices].shape) # 

mask[0, 0] = 1
mask[4, 5] = 1
mask[3, 2] = 1
mask[4, 3] = 1

indices = mask.nonzero()
print("indices shape: ", indices.shape)
print( "img_obs shape: ", img_obs.shape) # 
print("img_obs[indices] shape: ", img_obs[indices].shape) # 


# %% tensor[indices] creates a new tensor
m, n = 3, 3  # for example
tensor = torch.arange(m * n).reshape(m *n, 1)
mask = [1, 3, 5]
print(tensor)
sub_tensor = tensor[mask]
print("sub_tensor: ", sub_tensor)
# Modify the sub_tensor
sub_tensor[1] = 999
print("\nModified sub_tensor:")
print(sub_tensor)
print("\nOriginal tensor after modifying sub_tensor:")
print(tensor)


# %%
