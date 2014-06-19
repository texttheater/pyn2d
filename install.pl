:- initialization(
    (  pack_install(pinyin)
    -> halt
    ;  halt(1)
    ) ).
