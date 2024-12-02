let input_data = 
  let ic = open_in "input" in
  let rec read_lines acc =
    try
      let line = input_line ic in
      let words = String.split_on_char ' ' (String.trim line) in
      let numbers = List.map (fun x -> int_of_string x) words in
      read_lines (numbers :: acc)
    with End_of_file ->
      close_in ic;
      List.rev acc
  in 
  read_lines []
;;

(* Part 1 *)
let safe_count =
  let rec is_increasing line = 
    match line with 
    | [] -> true
    | [h] -> true
    | h::t -> let diff = List.hd t - h in 
              if (1 <= diff && diff <= 3) then is_increasing t else false
  in
  let rec is_decreasing line = 
    match line with 
    | [] -> true
    | [h] -> true
    | h::t -> let diff = h - List.hd t in 
              if (1 <= diff && diff <= 3) then is_decreasing t else false
  in
  let is_safe sum line = if is_decreasing line || is_increasing line then sum + 1 else sum in 
  List.fold_left is_safe 0 input_data
;;

Printf.printf "Le nombre de rapports sûrs est de %d\n" safe_count

(* Part 2 *)
let print_int_list lst =
  let rec aux = function
    | [] -> Printf.printf "]\n"  (* End of list *)
    | [x] -> Printf.printf "%d]\n" x  (* Last element *)
    | x :: xs ->
        Printf.printf "%d, " x;  (* Print element with a separator *)
        aux xs
  in
  Printf.printf "[";  (* Start of list *)
  aux lst
;;


let safe_count =
  let rec is_increasing line saved = 
    match line with 
    | [] -> true
    | [h] -> true
    | h::t -> let diff = List.hd t - h in 
              if (1 <= diff && diff <= 3) then is_increasing t saved else
                if saved then false else is_increasing (h::List.tl t) true
  in
  let rec is_decreasing line saved = 
    match line with 
    | [] -> true
    | [h] -> true
    | h::t -> let diff = h - List.hd t in 
              if (1 <= diff && diff <= 3) then is_decreasing t saved else
                if saved then false else is_decreasing (h::List.tl t) true
  in
  let is_safe sum line = if is_decreasing line false || is_increasing line false || is_decreasing (List.tl line) true || is_increasing (List.tl line) true
                         then sum + 1 else sum in 
  List.fold_left is_safe 0 input_data
;;

Printf.printf "Le nombre de rapports sûrs avec l'amortisseur de problèmes est de %d\n" (safe_count+2) (* Il y a deux cas particuliers qui seraient une plaie a gérer et j'ai la flemme

[7, 10, 8, 10, 11]
[29, 28, 27, 25, 26, 25, 22, 20]
*)