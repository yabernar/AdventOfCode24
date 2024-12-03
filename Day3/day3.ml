#load "str.cma";;

let input_data = 
  let ic = open_in "input" in
  let rec read_lines acc =
    try
      let line = input_line ic in
      read_lines (line :: acc)
    with End_of_file ->
      close_in ic;
      List.rev acc
  in 
  read_lines []
;;

(* Part 1 *)
let regex = Str.regexp "mul([0-9]+,[0-9]+)"

let search_next str i = 
  (Str.search_forward regex str i, Str.matched_string str)

let rec compute_line sum str =
  let rec process_next_match sum str start=
    try
      let (idx, text) = search_next str start in
      let text = String.split_on_char ',' text in 
      let left = int_of_string (List.nth (String.split_on_char '(' (List.hd text)) 1) in
      let right = int_of_string (List.nth (String.split_on_char ')' (List.nth text 1)) 0) in
      let res = sum + left * right in
      process_next_match res str idx+1 
    with Not_found ->
      sum
  in
  process_next_match sum str 0
;;
let mul_list = List.fold_left compute_line 0 input_data

(* Give up *)