# all_conf_template
a latex paper template that supports various conferences across research fields including computer graphics,  computer vision, and hci.

**still under construction**.

### How to use
To switch to different conference, you only need to go to `conf_preamble.tex`, and replace **siggraph** in the following line with some conference/journal name (please check the supportted conference/journal name listed below) you want to submit to.
```
\newcommand{\conf}{siggraph} -> \newcommand{\conf}{cvpr} ## if you want to submit to cvpr
```
And the template will take care of the rest.

To edit the title and authors information, you can go to the `xxx_metadata.tex`, where xxx is the name of the conference you want to submit to.

For ACM conferences and CVPR, you can edit the submission number in `xxx_preamble.tex`.
For ECCV, you can find the submission number in `eccv_preamble.tex`.
For cgf series (EG, PG, and so on), you can change the submission number in `cgf_metadata.tex`.


### supported conf
* siggraph/tog
* cvpr
* eccv
* uist
* tvcg
* cgf series
* chi

### prepare to support conf
- [ ] iccv (should be supported by the cvpr template already, need to confirm  detailed difference)
- [ ] cscw
- [ ] other IEEE transaction??
- [ ] ML conf (Neurips, ICML, ICLR, AAAI, IJCAI?)

### TODOs
- [ ] better support teaser.
- [ ] make another macro that is compatible with most of the conf sty files.
- [ ] write a simple tutorial for stage.
- [ ] check what is the best way to update sty files for each year.
- [ ] how to connect to overleaf?

If you have any questions/comments/bug reports, feel free to open a github issue or e-mail to the author I-Chao Shen (ichao.shen@ui.is.s.u-tokyo.ac.jp)
