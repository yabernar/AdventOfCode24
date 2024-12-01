(* Open the input file *)
let read_file filename =
  let ic = open_in filename in
  let rec read_lines acc_gauche acc_droite =
    try
      let line = input_line ic in
      let words = String.split_on_char ' ' (String.trim line) in
      match List.filter (fun x -> x <> "") words with
      | [g; d] -> read_lines (int_of_string g :: acc_gauche) (int_of_string d :: acc_droite)
      | _ -> failwith "Invalid line format"
    with End_of_file ->
      close_in ic;
      (List.rev acc_gauche, List.rev acc_droite)
  in
  read_lines [] []
;;

(* Part 1: Calculate the distance between the two lists *)
let calculate_distance gauche droite =
  let sorted_gauche = List.sort compare gauche in
  let sorted_droite = List.sort compare droite in
  List.fold_left2 (fun acc g d -> acc + abs (g - d)) 0 sorted_gauche sorted_droite
;;

(* Part 2: Calculate the similarity between the two lists *)
let calculate_similarity gauche droite =
  let droite_counts =
    List.fold_left
      (fun acc x -> 
        let count = try List.assoc x acc with Not_found -> 0 in
        (x, count + 1) :: List.remove_assoc x acc)
      [] droite
  in
  List.fold_left
    (fun acc g -> 
      let count = try List.assoc g droite_counts with Not_found -> 0 in
      acc + g * count)
    0 gauche
;;

(* Main function *)
let () =
  let (gauche, droite) = read_file "Day1/input" in

  (* Part 1 *)
  let distance = calculate_distance gauche droite in
  Printf.printf "La distance entre les listes est de %d\n" distance;

  (* Part 2 *)
  let similarity = calculate_similarity gauche droite in
  Printf.printf "La similarité entre les listes est de %d\n" similarity
;;
