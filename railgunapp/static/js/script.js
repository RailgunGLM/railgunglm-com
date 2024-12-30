const toggle = document.querySelector('.navbar .toggle');
const dropDownMenu = document.querySelector('.dropdown_menu');
const qlist = document.getElementById('qlist');
const startBtn = document.querySelector('.start');
const module = document.getElementById('module');
const topic = document.getElementById('topic');
const qno = document.getElementById('qno');
const qWrapper = document.getElementById('question-wrapper');
const settings = document.getElementById('settings');
const nxtBtn = document.querySelector('.next');
const finalScore = document.querySelector('.final-score');
const totalScore = document.querySelector('.total-score');
const endScreen = document.getElementById('end-screen');
const restartBtn = document.querySelector('.restart');
const subjectObject = {
    "Information Processing": ["Introduction to Information Processing", "Data Organization and Data Control", "Number and Character Encoding System", "Multimedia Elements and Digitization", "Spreadsheet", "Database"],
    "Computer System Fundamentals": ["Computer Hardware", "Input and Output Devices", "Computer Software"],
    // secondary storage devices -> include into system unit of computer -> name change to computer hardware
    "Internet and its Applications": ["The Networking and Internet Basics", "Internet Services and Applications", "Elementary Web Authoring", "Threats and Security on the Internet"],
    // Introduction to HTML -> include into elementary web authoring, communication software and protocols -> The Networking and Internet Basics
    "Computational Thinking and Programming": [], // omitted
    "Social Implications": ["Technological Innovations", "Health and Ethical Issues", "Intellectual Property"]
}
window.onload = function () {
    for (var x in subjectObject) {
        module.options[module.options.length] = new Option(x, x);
    }
    module.onchange = function () {
        qno.length = 1;
        topic.length = 1;
        var y = subjectObject[this.value];
        for (var i = 0; i < y.length; i++) {
            topic.options[topic.options.length] = new Option(y[i], y[i]);
        }
        if (module.value != 'Select module' && topic.value != 'Select topic' && qno.value != 'Select number of questions') {
            startBtn.disabled = false;
        } else {
            startBtn.disabled = true;
        }
    }
    topic.onchange = function () {
        qno.length = 1;
        fetch('https://res.cloudinary.com/dxhkoqh3v/raw/upload/v1734381545/railgunglm/data/bmcdivc7ctdan3hj0mwd.json')
        .then(response => response.json())
        .then(data => {
            questions = data;
            questions = questions.filter(item => item.topic == topic.value);
            for (var i = 1; i <= questions.length; i++) {
                qno.options[i] = new Option(i, i);
            }
        })
        .catch(error => {
            console.error('Error fetching questions.json: ', error);
        });
        if (module.value != 'Select module' && topic.value != 'Select topic' && qno.value != 'Select number of questions') {
            startBtn.disabled = false;
        } else {
            startBtn.disabled = true;
        }
    }
    qno.onchange = function () {
        if (module.value != 'Select module' && topic.value != 'Select topic' && qno.value != 'Select number of questions') {
            startBtn.disabled = false;
        } else {
            startBtn.disabled = true;
        }
    }
}
let questions,
    current,
    score = 0;
toggle.onclick = function () {
    dropDownMenu.classList.toggle('open');
}
const startQuiz = () => {
    fetch('https://res.cloudinary.com/dxhkoqh3v/raw/upload/v1734381545/railgunglm/data/bmcdivc7ctdan3hj0mwd.json')
        .then(response => response.json())
        .then(data => {
            questions = data;
            if (module.value == 'Select module'){
                alert ('Error: module not selected');
                return;
            }
            if (topic.value == 'Select topic'){
                alert ('Error: topic not selected');
                return;
            }
            if (qno.value == 'Select number of questions'){
                alert ('Error: number of questions not selected');
                return;
            }
            settings.classList.add("hide");
            qWrapper.classList.remove("hide");
            questions = questions.filter(item => item.topic == topic.value);
            for (let i = questions.length - 1; i > 0; i--) {
                let j = Math.floor(Math.random() * (i + 1));
                [questions[i], questions[j]] = [questions[j], questions[i]];
            }
            while (questions.length > parseInt(qno.value)) {
                questions.pop();
            }
            current = 1;
            showQuestion(questions[0]);
        })
        .catch(error => {
            console.error('Error fetching questions.json: ', error);
        });
};
startBtn.addEventListener("click", startQuiz);
const showQuestion = (question) => {
    const questionText = document.querySelector('.question'),
        answerWrapper = document.querySelector('.answer-wrapper'),
        questionNumber = document.querySelector('.number');
    questionText.innerHTML = question.question;
    const answers = [...question.incorrect_answers, question.correct_answer.toString()];
    for (let i = answers.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [answers[i], answers[j]] = [answers[j], answers[i]];
    }
    answerWrapper.innerHTML = '';
    let cnt = 0, cnt1 = 0, ans;
    answers.forEach((answer) => {
        answerWrapper.innerHTML += `<label class="radio"><div class="answer"><input type="radio" style="display: none;" name="answer" value="${answer}"><span class="text">${answer}</span></div></label>`;
        if(answer == question.correct_answer.toString()) ans = cnt;
        cnt++;
    });
    questionNumber.innerHTML = `Question <span class="current">${current}</span><span class="total">/${questions.length}</span>`;
    const answersDiv = document.querySelectorAll('.answer');
    nxtBtn.disabled = true;
    var answered = false;
    answersDiv.forEach((answer) => {
        answer.addEventListener("click", () => {
            if (!answered) {
                if (document.querySelector('input[name="answer"]:checked').value == question.correct_answer.toString()) {
                    score++;
                    answer.classList.add('correct');
                } else {
                    answer.classList.add('incorrect');
                    answersDiv.forEach((answer) => {
                        if(cnt1 == ans) answer.classList.add('correct');
                        cnt1++;
                    });
                }
                var btns = document.getElementsByName('answer');
                for (let i = 0; i < btns.length; i++) {
                    btns[i].disabled = true;
                }
                answered = true;
                nxtBtn.disabled = false;
            }
        });
    });
};
nxtBtn.addEventListener("click", () => {
    nextQuestion();
});
const nextQuestion = () => {
    if (current < questions.length) {
        current++;
        showQuestion(questions[current - 1]);
    } else {
        showScore();
    }
};
const showScore = () => {
    qWrapper.classList.add("hide");
    endScreen.classList.remove("hide");
    finalScore.innerHTML = score;
    totalScore.innerHTML = '/' + questions.length.toString();
    if (5 * score >= 4 * questions.length){
        finalScore.classList.add("good-score");
        totalScore.classList.add("good-score");
    }else{
        finalScore.classList.remove("good-score");
        totalScore.classList.remove("good-score");
    }
};
restartBtn.addEventListener("click", () => {
    window.location.reload();
});
