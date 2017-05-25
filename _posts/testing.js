/*
Friday test: OOJ

When the document is ready

1. representing data from the api - model
2. our views - what the user sees - view
3. Passing back and forth - controller

src/views/CatchPhraseView.js
src/views/CatchPhraseModel.js
link in HTML via script tag (same as index.js)

class CatchPhrase {

  static all(callbackFn) {
    $.ajax({
        url: 'http://localhost:3000/api/v1/catch_phrases',
        success: callbackFn
    })
  }

}

static = makes it a class level method

class CatchPhraseView {

  contructor(phrase)
    { this.phrase = phrase }

  render()
    { return `<li>${this.phrase.content}</li>` }

}


$function(){

  catchPhrase.all( data => {

  })

}

*/

<html>

  <div class='container'>
    <h1>Catch Phraser</h1>

    <div class='row'>
      <div class='col s4'>
        <h2>Where the Form Goes</h2>
        <form id='new-phrase'>
          <input type='text' placeholder='Content' name='content' />
          <input type='text' placeholder='Student Name' name='student_name' />
          <input type='submit' value="Create Phrase" />
        </form>
      </div>

      <div class='col s8'>
        <ul id='phrases'>
        </ul>


      </div>

    </div>
  </div>

</html>

$.ajax({
    url: 'http://localhost:3000/api/v1/catch_phrases',
    success: data => {
        data.forEach (phrase => {
            $('#phrases').append(`<li>${phrase.content}</li>`)
        })
    }
})

$('#new-phrase').on('submit', event => {
  event.preventDefault()
  const content = $('input[name=content]').val()
  const studentName = $('input[name=student_name]').val()
  if (content.length && studentName.length) {
    $.ajax({
      url: 'http://localhost:3000/api/v1/catch_phrases',
      method: 'POST',
      data: {
        catch_phrase:
          { content: content },
          { student: studentName }
        }
      }
      success: phrase => {
        $('#phrases').append(`<li>${data.content}</li>`)
        $('input')
      }
    })
    $('#error').html("")
  } else {
    $('#error').html('You must fill out both fields')
  }
  console.log()
})
