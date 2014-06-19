all : pyn2d pyn2d.plugin
	@echo BUILD SUCCESSFUL
	@echo To complete installation,
	@echo 1\) make sure the compiled pyn2d is on your PATH
	@echo 2\) use Mnemosyne\'s plugin manager to install pyn2d.plugin

pyn2d : pyn2d.pl install_pinyin
	swipl -l $< -g "qsave_program('$@', [stand_alone(true), goal(main)]), halt"

install_pinyin :
	swipl -l install

pyn2d.plugin : pyn2d.py
	zip $@ $<
