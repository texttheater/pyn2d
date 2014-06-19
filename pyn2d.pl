:- use_module(library(pinyin), [
	num_dia/2]).

main :-
  current_prolog_flag(os_argv, [_,File]),
  see(File),
  process_remaining_lines,
  seen,
  halt.
main :-
  format(user_error, 'Usage: pinyin_num2dia FILE~n', []),
  halt(1).

process_remaining_lines :-
  current_input(Stream),
  read_line_to_codes(Stream, Codes),
  continue(Codes).

continue(end_of_file) :-
  !.
continue(InputLine) :-
  num_dia(InputLine, OutputLine),
  atom_codes(OutputAtom, OutputLine),
  write(OutputAtom),
  nl,
  process_remaining_lines.
