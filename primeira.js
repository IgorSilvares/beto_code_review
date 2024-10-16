/*
1) Given an array of strings, write a function which removes the duplicates.
For example, given the input = ["hello","hello", "world"], the output = ["hello", "world"]
*/


function remove_duplicates(input){
    let unique = []
    for (let i = 0; i < input.length; i++) {
      if (!unique.includes(input[i]))
        unique.push(input[i])
    }
    return unique
  }
  
  const input = ["hello","hello", "world"];
  const result = remove_duplicates(input)
  console.log(result)