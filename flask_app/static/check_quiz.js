btn_check = document.getElementById("btn_check")

function check_quiz() {
    var correct_answers = 0

    ol = document.getElementsByTagName("ol")[2]
    li = ol.children
    for (let i=0 ; i<li.length - 1 ; i++) {
        var quiz_li = li[i] // Direct li element of ol tag
        options = quiz_li.getElementsByTagName("li") // inside each quiz_li there is ul which contains all options as li tag

        var checked_input_li = false;
        var correct_input_li = false;
        var correct = false;

        options.forEach(element => {
            input = element.getElementsByTagName("input")[0]
            input.disabled = "disabled"

            if (input.value == 1) {
                correct_input_li = element
            }
            if (input.checked) {
                checked_input_li = element
                if (input.value == 1) {
                    correct_answers++
                    element.classList.add("wpProQuiz_answerCorrect");
                    correct = true
                }
            }
        });

        resp_div = quiz_li.getElementsByClassName("wpProQuiz_response")[0]
        // console.log(quiz_li)
        // return 0

        resp_div.style.display = "block"
        correct_div = resp_div.children[0]
        incorrect_div = resp_div.children[1]

        if (correct == false) {
            correct_input_li.classList.add("wpProQuiz_answerCorrectIncomplete")
            incorrect_div.style.display = "block"
            if (checked_input_li != false) // Check if user checked radio input or not
                checked_input_li.classList.add("wpProQuiz_answerIncorrect")
        }
        else {
            correct_div.style.display = "block"
        }
    }

    return correct_answers
}

btn_check.onclick = ()=> {
    var correct_answers = check_quiz()
    console.log(correct_answers)
}