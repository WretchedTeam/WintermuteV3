init python:
    consulai_start_email = Email(
        unique_id="consulai_start_email",
        subject="URGENT v0.5.2 upd",
        contents="""
It's Iwan. I've read through your feedback for the nickname test, and…to put it lightly, {i}holy shit{/i}. I’ve reverted the entire build back to about two hours before Jeremy pushed his sludge, so we should have reverted whatever damage was done.

But if anything like that ever happens again then abort the sim and email me --immediately--. I am not having Jeremy jeopardize our branch by pushing substandard shit again. Got it?

For the moment, I’ve got something else. Personal feelings about e-therapists aside, I’ve been asked to have you stress test Wintermute’s integration with our old ConsulAI framework that was built into the John M chatbot, from way back when. We know who we’re selling virtual girlfriends to. It’s a necessary feature.

So, here’s what you need to do. Before you start, you’ll need to enable our "depressed user" customer profiling preset. Tell them you’re sad, and stick to the sob script on the post-it note I left on your desk. After that, just let the Doki try and ‘console’ you and send it back to me. Barring any blatant issues, I’ll relay the results to our psych adviser for the green light.

- IG
""",
        sender=igreen_sender,
        is_important=True
    )

    consulai_final_email = Email(
        unique_id="consulai_final_email",
        subject="Mental Health",
        contents="""
Hey all, I know we're still reeling from hearing about James' passing. I only just came back from leave, as I was hit hard by this. Those who knew him were fortunate to meet such a smart and focused guy. Even though he was let go, he's still part of the Turnell family for me. We'll miss him a lot. We have a card in the break room for us to sign for his family, and I'll personally deliver it after lunch today.

Given that James was struggling with mental health issues relating to the WM project, we feel it's necessary to perform a mental wellness evaluation on our employees. We'll have an official HR meeting about it next week. It's required attendance, so be there. But just to be quick about things: depression is a very real and valid problem that can affect anyone invisibly, and historically IT work correlates with depression and a feeling of isolation. Depression can manifest itself in many ways:

- Feeling worthless, like a failure, that the world would be better off without you
- A desire to hurt yourself or end your own life
- Inappropriate emotional bonds towards inanimate objects or software
- Constant paranoia and feeling of being watched
- Having little to no interest in work, hobbies, or activities
- Assigning significant attachment and meaning to meaningless statements
- Trouble falling or staying asleep
- Over-attachment to a personality, such as a celebrity or streamer

If you're feeling any of these symptoms, please reach out to our Mental Health Helpline: mentalhealth@turnelltech.co.uk. They can schedule you a meeting with one of our licensed therapists, who are happy to help. It's anonymous, so feel free to reach out.

Have a great start to your day!

-Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        quick_replies=[
            EmailReply("Thank you.", Jump("script5_post_finish")),
            EmailReply("I'm sorry.", Jump("script5_post_finish")),
            EmailReply("RIP.", Jump("script5_post_finish")),
        ],
        receiver="@TurnellQA"
    )