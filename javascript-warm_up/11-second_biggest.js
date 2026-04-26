#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {


    const args = process.argv.slice(2).map(Number);

  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);

  if (uniqueSorted.length > 1) {
    console.log(uniqueSorted[1]);
  } else {
    console.log(0);
  }
}
