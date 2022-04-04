{% for key,value in item.question.questions.items %}
        <div id="question_div-{{forloop.counter}}" class="col-md-3 questions">
          <div class="inputgroup mt-4">
              
              <label id="id_question_number-{{forloop.counter}}">{{forloop.counter}}. Soru</label>
              <div class="input-icon">
                <input type="text" name="question-{{forloop.counter}}" class="form-control" id="id_question-{{forloop.counter}}" placeholder="Soru" value="{{key}}">
                <span>
                  <i class="flaticon-questions-circular-button icon-md"></i>
                </span>
              </div>
              <button class="btn btn-sm btn-outline-secondary mt-2" type="button" onclick="appendAnswer({{forloop.counter}})">Cevap Şıkkı Ekle</button> 
              <br>
              <div class="answer-{{forloop.counter}} answers" id="id_answer-{{forloop.counter}}">
                {% for answer in value %}
                <input type="text" class="form-control mt-2" value="{{answer}}" name="answer-{{forloop.counter}}" placeholder="Cevap Şıkkı">
                {% endfor %}
              </div>
           </div>
        </div>
        {% endfor %}
