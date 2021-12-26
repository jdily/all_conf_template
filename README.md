# all_conf_template
a latex paper template to support various conferences across fields including computer graphics,  computer vision, and hci.

**still under construction**.

### How to use
To switch to different conference, you only need to go to `conf_preamble.tex`, and replace **siggraph** in the following line with some conference/journal name (please check the supportted conference/journal name listed below) you want to submit to.
```
\newcommand{\conf}{siggraph} -> \newcommand{\conf}{cvpr} ## if you want to submit to cvpr
```
And the template will take care of the rest.


### supported conf
* siggraph/tog
* cvpr
* eccv
* uist
* tvcg
* cgf series

### prepare to support conf
- [ ] iccv (should be supported by the cvpr template already, need to confirm  detailed difference)
- [ ] chi (should be supported by acmart already, need to confirm detailed difference)
- [ ] other IEEE transaction??

### TODOs
- [ ] better support teaser.
- [ ] make another macro that is compatible with most of the conf sty files.
- [ ] write a simple tutorial for stage.
- [ ] check what is the best way to update sty files for each year.
