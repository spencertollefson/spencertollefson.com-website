# All about the $AJAX

The way we will connect JS to our Flask app is by using AJAX (**A**synchronous **J**avascript **A**nd **X**ML), which will access using JQuery.

To get access to JQuery, we will need the following code in our HTML:
```html
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
```

The AJAX call has the form
```javascript
$.ajax({
  type: "POST",
  contentType: "application/json; charset=utf-8",
  url: "/score",  // Replace with URL of POST handler
  dataType: "json",
  async: true,
  data: JSON.stringify(
    /*
      Object or Array you want to pass
    */),
  success: (result) => {
    /*
    function to run with returned object
    from your POST request to Flask if successful. Success determined by status code

    Should probably use JQuery to update
    page information
    */
  },
  error: (result) => {
    /*
    function to run with returned object
    from your POST request if there was a failure
    */
  }
})
```
