


async function get_text(){

    query_value = document.getElementById("search").value;
    amount_value = document.getElementById("amount").value;

    let python_func = await eel.scraper(query_value, amount_value)();

    let counter = python_func[3]
    let group_counter = 0;

    for(let i = 0; i < counter; i++){

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
        div_res.className = 'result';

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

        if(i == 0) {
            main_div.append(div_group);
            div_group.append(div_group_title);
            div_group_title.append(p_group_title);
            div_group_title.append(img_arrow_down);
        }
        else if(i % amount_value == 0){
            main_div.append(div_group);
            div_group.append(div_group_title);
            div_group_title.append(p_group_title);
            div_group_title.append(img_arrow_down);
            group_counter++;
        }

        div_group.append(div_res);
        div_res.append(div_wrap);
        div_wrap.append(div_title_img);
        div_title_img.append(res_title);
        div_title_img.append(res_img);
        div_wrap.append(res_text);

        let func_title = python_func[0][i];
        let func_img = python_func[1][i];
        let func_text = python_func[2][i];
        let query_return = python_func[4][group_counter];

        res_title.innerText = func_title;
        res_img.src = func_img;
        res_img.className = "article_img";
        res_text.innerText = func_text;
        p_group_title.innerText = query_return;
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

$(".group_title_container").click(function(){
    $(this).toggleClass("group_title_container_active");
    $(this).find(".arrow_down").toggleClass("arrow_up");
})