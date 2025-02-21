import time


def html_title(text: str) -> str:
    html_title_str = (f"""
    <style>
    .title {{
        font-size: 1.17em; 
        font-weight: bold; 
        margin-bottom: 1em; 
    }}
    </style>
    <div className=title>{text}</div>
    """)
    
    return html_title_str


def html_result(result: str, emoji: str) -> str:
    unique_id = "".join(str(time.time()).split("."))

    html_result_str = (f"""
    <style>
    @keyframes fadeInUp-{unique_id} {{
        0% {{
            transform: translateY(100%);
            opacity: 0;
        }}
        100% {{
            transform: translateY(0%);
            opacity: 1;
        }}
    }}

    .fadeInUp-animation-{unique_id} {{
        animation: 1.5s fadeInUp-{unique_id};
        font-size: 1.5em;
        margin-top: 0.5em;
    }}
    </style>
    
    <div className="fadeInUp-animation-{unique_id}">Your text is <b>{result}</b> {emoji}</div>
    """)

    return html_result_str