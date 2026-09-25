"""DiffCR's denoising network and sampler as an installable package.

`nafnet_double_encoder_splitcaCond_splitcaUnet.UNet` (the network of the released DiffCR model,
config/ours_sigmoid.json) and `dpm_solver_pytorch` (the DPM-Solver++ sampler DiffCR uses) are
symlinks to the unchanged upstream files in `models/ours/` and `core/`; the diffusion wrapper
(models/network_x0_dpm_solver.py) imports `core` by its top-level name, so it stays with the
scripts. The scripts' dependencies stay in the `scripts` dependency group.
"""
