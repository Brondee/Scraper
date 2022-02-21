


async function get_text(){

    var resources_check = [];

    //getting all resources buttons
    let first_resource = document.getElementsByClassName("resource")[0];
    let second_resource = document.getElementsByClassName("resource")[1];

    //checking if each resource has been chosen
    if (first_resource.classList.contains("resource_active")){
        resources_check.push("1");
    }
    if (second_resource.classList.contains("resource_active")){
        resources_check.push("2");
    }

    //getting query value and the amount of articles to return
    query_value = document.getElementById("search").value;
    amount_value = document.getElementById("amount").value;

    //calling python function
    let python_func = await eel.config(query_value, amount_value, resources_check)();

    let counter = python_func[3]
    let group_counter = 0;
    
    //group open/close function
    function open(){
        $(this).toggleClass("group_title_container_active");
        $(this).find(".arrow_down").toggleClass("arrow_up");
        $(this).parent().find(".result_hidden").toggleClass("result");
    }

    //for each article 
    for(let i = 0; i < counter; i++){

        //creating all necessary elements to show article's info
        let div_group = document.createElement("div");
        div_group.className = "group_container";

        let div_group_title = document.createElement("div");
        div_group_title.className = "group_title_container";

        let p_group_title = document.createElement("p");
        p_group_title.className = "group_title";

        let img_arrow_down = document.createElement("img");
        img_arrow_down.className = "arrow_down";
        img_arrow_down.src = "icons/arrow-down.png";

        let div_res = document.createElement('div');
        div_res.className = 'result_hidden';

        let div_wrap =  document.createElement('div');
        div_wrap.className = "result_wrap";

        let div_title_img = document.createElement('div');
        div_title_img.className = "title_img_block";

        let res_title = document.createElement('h3');
        res_title.className = 'result_title';

        let res_img = document.createElement('img');
        res_img.className = 'article_img_hidden';

        let res_text = document.createElement('p');
        res_text.className = 'main_text';

        let main_div = document.getElementsByClassName("results")[0];

        //grouping articles by query function
        if(i == 0) {
            main_div.append(div_group);
            div_group.append(div_group_title);
            div_group_title.append(p_group_title);
            div_group_title.append(img_arrow_down);
        }
        else if(i % (amount_value * resources_check.length) == 0){
            main_div.append(div_group);
            div_group.append(div_group_title);
            div_group_title.append(p_group_title);
            div_group_title.append(img_arrow_down);
            group_counter++;
        }

        div_group = document.getElementsByClassName("group_container")[group_counter];
        
        //appending all elements
        div_group.append(div_res);
        div_res.append(div_wrap);
        div_wrap.append(div_title_img);
        div_title_img.append(res_title);
        div_title_img.append(res_img);
        div_wrap.append(res_text);

        //appending all article's info to variables
        let func_title = python_func[0][i];
        let func_img = python_func[1][i];
        let func_text = python_func[2][i];
        let query_return = python_func[4][group_counter];

        //appending all article's info to elements in webpage
        res_title.innerText = func_title;
        res_img.src = func_img;
        res_img.className = "article_img";
        res_text.innerText = func_text;
        p_group_title.innerText = query_return;

        //adding click event to group div
        group_clicker = document.getElementsByClassName("group_title_container")[group_counter];
        group_clicker.addEventListener('click', open)
    }
}

$(".choice").click(function(){
    $(this).addClass("choice_active").siblings().removeClass("choice_active");
    let choice_value = $(this).find(".choice_txt").text();
    $("#search").val(choice_value);
})

$("#submit").click(function(){
    get_text();
})

$("#search").click(function(){
    $(".choice").removeClass("choice_active");
})

$(".resource").click(function(){
    $(this).toggleClass("resource_active");
})

$(window).scroll(function(){
    if ($(this).scrollTop() > 900){
        console.log("yes");
        $(".scroll_top")[0].style.display = "flex";
    } else{
        $(".scroll_top")[0].style.display = "none";
    }
})

$(".scroll_top").click(function(){
    $("html, body").animate({
        scrollTop: $($(this).attr("href")).offset().top + "px"
    }, {
        duration: 400,
        easing: "swing"
    });
    return false;
});
