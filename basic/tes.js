let arr = ["www.google.co.id", "www.facebook.com"]
arr.forEach(item => {
  let newArr = item.split(".")
  let host = newArr[1]
  console.log(host);
})