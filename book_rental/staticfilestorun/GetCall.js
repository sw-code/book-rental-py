//Get
const asyncGetCall = async () => {
    try {
       const response = await fetch('/api/books');
       const data = await response.json();
       console.log(data[0].id);
       return data;
      } catch(error) {
         console.log(error);
      }
}
//asyncGetCall()