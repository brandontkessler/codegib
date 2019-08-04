def create_seed_users(db, user_model):
    user1 = user_model(email='user1@test.com', password='password',
        confirmed=True, admin_priv=True, blog_priv=True)
    user2 = user_model(email='user2@test.com', password='password',
        confirmed=True, admin_priv=False, blog_priv=True)
    user3 = user_model(email='user3@test.com', password='password',
        confirmed=True, admin_priv=False, blog_priv=False)
    user4 = user_model(email='user4@test.com', password='password',
        confirmed=True, admin_priv=False, blog_priv=False)

    for user in user1,user2,user3,user4:
        db.session.add(user)

    db.session.commit()

def create_seed_blogs(db, blog_model):
    blog1 = blog_model(title="This is the first title to This Blog",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Andouille jowl ham burgdoggen sirloin jerky chicken rump boudin ham hock. Meatloaf beef ribs tongue jowl, turkey bacon pork chop capicola t-bone chuck buffalo ball tip. Hamburger shoulder pastrami porchetta chicken. Spare ribs tri-tip hamburger bacon, swine turkey turducken brisket drumstick picanha.

            Pig cupim hamburger short ribs venison, spare ribs meatball strip steak boudin kevin short loin ham flank tongue. Venison cupim swine landjaeger, ground round meatloaf shoulder pastrami turkey buffalo salami biltong pork belly. Hamburger ham porchetta frankfurter brisket, leberkas salami turducken ham hock sausage bacon pork belly jerky. Porchetta alcatra shoulder ham meatball kevin corned beef. Beef ribs pancetta meatloaf meatball shank, tail short loin chuck filet mignon pig cupim turducken. Prosciutto brisket filet mignon, jowl shoulder chuck frankfurter shank pork chop short loin t-bone biltong fatback kevin. Shoulder pastrami filet mignon pork, capicola ground round turducken biltong short loin pork loin ham pork belly cupim strip steak.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;python;mining',
        user_id=2)
    blog2 = blog_model(title="Whoa Whoa Hey Hey",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;python;mining;other;analysis',
        user_id=2)
    blog3 = blog_model(title="3 Bloga and aowiefhoaiwhofihawoihaew",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;spider;strategy',
        user_id=1)

    blog4 = blog_model(title="4 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Andouille jowl ham burgdoggen sirloin jerky chicken rump boudin ham hock. Meatloaf beef ribs tongue jowl, turkey bacon pork chop capicola t-bone chuck buffalo ball tip. Hamburger shoulder pastrami porchetta chicken. Spare ribs tri-tip hamburger bacon, swine turkey turducken brisket drumstick picanha.

            Pig cupim hamburger short ribs venison, spare ribs meatball strip steak boudin kevin short loin ham flank tongue. Venison cupim swine landjaeger, ground round meatloaf shoulder pastrami turkey buffalo salami biltong pork belly. Hamburger ham porchetta frankfurter brisket, leberkas salami turducken ham hock sausage bacon pork belly jerky. Porchetta alcatra shoulder ham meatball kevin corned beef. Beef ribs pancetta meatloaf meatball shank, tail short loin chuck filet mignon pig cupim turducken. Prosciutto brisket filet mignon, jowl shoulder chuck frankfurter shank pork chop short loin t-bone biltong fatback kevin. Shoulder pastrami filet mignon pork, capicola ground round turducken biltong short loin pork loin ham pork belly cupim strip steak.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;python;mining',
        user_id=2)

    blog5 = blog_model(title="5 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;python;mining;other',
        user_id=2)

    blog6 = blog_model(title="6 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all',
        user_id=1)

    blog7 = blog_model(title="7 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Andouille jowl ham burgdoggen sirloin jerky chicken rump boudin ham hock. Meatloaf beef ribs tongue jowl, turkey bacon pork chop capicola t-bone chuck buffalo ball tip. Hamburger shoulder pastrami porchetta chicken. Spare ribs tri-tip hamburger bacon, swine turkey turducken brisket drumstick picanha.

            Pig cupim hamburger short ribs venison, spare ribs meatball strip steak boudin kevin short loin ham flank tongue. Venison cupim swine landjaeger, ground round meatloaf shoulder pastrami turkey buffalo salami biltong pork belly. Hamburger ham porchetta frankfurter brisket, leberkas salami turducken ham hock sausage bacon pork belly jerky. Porchetta alcatra shoulder ham meatball kevin corned beef. Beef ribs pancetta meatloaf meatball shank, tail short loin chuck filet mignon pig cupim turducken. Prosciutto brisket filet mignon, jowl shoulder chuck frankfurter shank pork chop short loin t-bone biltong fatback kevin. Shoulder pastrami filet mignon pork, capicola ground round turducken biltong short loin pork loin ham pork belly cupim strip steak.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        _tags='all;python;mining;strategy',
        user_id=2)

    blog8 = blog_model(title="58 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        tags='python, mining, other',
        user_id=2)
    blog9 = blog_model(title="9 Blogasdf",
        headline="""
            Bacon ipsum dolor amet alcatra frankfurter leberkas spare ribs. Shankle bresaola swine, jerky boudin spare.
        """,
        _content="""Bacon ipsum dolor amet shank jerky porchetta pork belly. Kielbasa sirloin chuck burgdoggen. Leberkas tongue ground round porchetta t-bone tenderloin ball tip pork belly. Filet mignon andouille tongue turkey, shoulder tenderloin frankfurter kielbasa tail landjaeger biltong bacon bresaola salami.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.

            Ham hock pork belly meatball, spare ribs porchetta shoulder short loin boudin pancetta venison strip steak short ribs prosciutto buffalo. Pig boudin picanha flank, fatback shankle biltong prosciutto brisket. Buffalo ribeye meatball ham hock ground round sirloin. Prosciutto short ribs ribeye pig corned beef alcatra biltong ground round tenderloin beef salami. Beef ribeye spare ribs salami, kielbasa ham hock pork chop pork brisket corned beef turkey frankfurter tenderloin shoulder prosciutto.

            Turducken spare ribs ham hock, frankfurter sirloin cupim boudin pig. Meatloaf sausage picanha short ribs ham hock meatball short loin porchetta ribeye ham brisket beef ribs andouille. Porchetta brisket t-bone flank, shoulder leberkas ribeye venison frankfurter jowl pancetta sausage kevin pork drumstick. T-bone meatball shoulder, shank burgdoggen beef pastrami tail kevin landjaeger ground round. Bresaola beef ribs cupim prosciutto shoulder pastrami, shankle sirloin. Turkey brisket cupim beef ribs pork loin shoulder meatloaf andouille. Bresaola meatloaf tenderloin ribeye pastrami chuck short loin venison short ribs pork belly hamburger ball tip picanha.
        """,
        tags='scraping, analysis',
        user_id=1)

    for blog in blog1,blog2,blog3,blog3,blog4,blog5,blog6,blog7,blog8,blog9:
        db.session.add(blog)

    db.session.commit()
