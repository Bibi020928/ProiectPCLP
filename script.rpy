# AICI AM DEFINIT CARACTERELE , CU OPTIUNEA "define"
define b = Character("Gică", color = "#FFFE00")
define p2 = Character("Ion", color = "#0064E9")
define p3 = Character("Mircea", color = "#0064E9")
define tu = Character("[nume]")
define f1 = Character("Roxana")
define v = Character("Maria", color="#c2ffc9")
define e = Character("Profesor")
define nec = Character("???")
define bus = Character("Domnu' șofer", color="#FFFFFF")
define vtu = Character("[v] și [tu]")

# AICI FOLOSIM ACEASTĂ OPTIUNE PENTRU A MICSORA O POZA A UNUI CARACTER
init -10 python:
    def embiggen(s):
        return Transform(s, zoom=0.8)
# SE FOLOSESTE PREFIX small PENTRU A PUTEA CREA O NOUA IMAGINE, FOLOSINDUSE DE PREFIX,
# SI FARA SA SE MAI CREEZE O ALTA IMAGINE DE TIP .jpg IN FOLDERUL JOCULUI
    config.displayable_prefix["small"] = embiggen

image sumi open small = "small:sumi open"

# INCEPUTUL JOCULUI

label start:
    # AICI AM DEFINIT O VARIABILA, CARE O SA O FOLOSIM PENTRU UN if
    default alegere = 0
    default muzica = 0
# ACEASTA OPTIUNE ESTE FOLOSITA PENTRU A DA UN NUME CARACTERULUI PRINCIUAL, ADICA "tu"
    stop music
    $nume = renpy.input("Cum te numesti?")
    if nume =="":
        "Intrudu un nume."

    scene black

    menu:
        "Dorești să foloseși versiunea jocului cu 'câteva' melodii Românești?":
             $muzica = 0

        "Dorești să nu apară melodii Românești în joc?":
            $muzica = 1



    "Totul a început atunci când am ales să ma duc în tabără pe timpul verii."

    "Am hotărât împreună cu câțiva prieteni să mergem într-o tabară despre supraviețuitul în pădure."

    scene statie1
    play music  "audio/Hokabi.mp3"

    tu "Hai mă mai repede odata, că pierdem autocarul."

    p3 "Stai mă așa că mai avem oleaca pană în stație. "

    p2 "Mai sunt doar 3 străzi."

    tu "Știu că putem face asta."

    tu "Haide baieții!!!"

    scene black

    "Am ajuns noi la stația de unde trebuia să luăm autocarul."

    play music "audio/Caged Heart.mp3"
    "Dar când să mai urc și eu șoferul a închis ușile și a spus că nu mai este loc și pentru mine."

    "Așa că am avut de ales."
    # CU OPTIUNEA MENU PUTEM ALEGE CE SE INTAMPLA IN CONTINUARE CU POVESTEA
    # jump ESTE FOLOSIT PENTRU A ACCESA ALEGERILE PE CARE LE-AM FACUT, APELAND LABELUL
    # CU ACELASI NUME
    menu:



         "Să îl sun pe Gică să mă ducă el cu mașina lui.":
            jump prieten

         "Să mă rog de șofer, că poate mă lasă și pe mine.":
            jump autobuz

    return
    label prieten:
        tu "Ce mai faci ma Gică, ai treabă acum?"

        b "Nu fra, da de ce?"

        b "Ai nevoie de ceva?"

        tu "Ai cum să mă duci și pe mine cu mașina până undeva?"

        b "Cum să nu, doar nu ești tu fratele meu."
        if muzica==0:

            play music "audio/Artileria.mp3"

        else:
            play music "audio/coolio.mp3"



        scene golf4gica

        "Peste 15 minute apare Gică cu un Golf4 negru cu spoiler."
        "Din care se auzea muzica la blana."

        b "Hai mă, ce mai aștepți?"

        tu "Gata acuma urc"

        "Îi pun eu pe Waze destinația, după care am ațipit."

        scene black

        "Peste vreo 2 ore mă trezesc și observ că Gică a ales să folosească o scurtătură, fără să se mai folosească de Waze."
        if muzica == 1:
            play music ["audio/eminem.mp3"] fadeout 1.0 fadein 1.0

        else:
            play music ["audio/Johnny Nebunu.mp3"] fadeout 1.0 fadein 1.0
        scene padure with fade

        tu "Ce faci mă, unde am ajuns?"

        b "Stai așa că stiu eu unde să te duc."

        scene black

        "Mai mergem noi vreo 10 minute și ajungem la poarta unei tabere."
        scene intrare
        "TABARA MESTEACĂNUL"

        tu "Unde m-ai adus mă?"

        tu "Nu asta e tabăra."

        b "Lasă că asta e."

        "Și se urcă în mașină și pleacă"

        stop music fadeout 2.0
        tu "BĂĂĂĂĂ, STAI AȘAAAAA!!!"

        jump tabara


        return

    label autobuz:
        tu "Haideți, vă rog eu frumos! Nu am cum să ajung altfel în tabără la timp!!"
        bus "Îmi pare rău, dar chiar nu mai am locuri libere, și în picioare nu te pot lăsa să stai.."
        tu "Dar să știți că am mai stat până acum în picioare, și nu am nicio problemă cu asta!!"
        tu "Haideți vă rog eu, faceți cumva și luați-mă și pe mine!!"
        bus "Zici că ai mai stat până acum în picioare?"
        tu "Daa, de mai multe ori chiar! Haideți, vă rog mult!"
        bus "No atunci hai, urcă, să nu te mai aud."
        scene drum1
        #play music alege tu una
        "..."
        tu "Am înțeles că va fi un drum lung, sper să rămân treaz până ajung acolo."
        tu " *Aghhh, îmi e cam somn."
        scene black
        "Și am adormit..."
        "După 2 ore simt niște mișcări bruște."
        scene autobus
        bus "Domnule! Treziță-vă!! Am ajuns deja de 10 minute! Tebuie să mă întorc!"
        tu "Aoleo. Deja am ajuns?"
        bus "Da, toți au plecat deja, după dumneavoastră aștept."
        tu "Vă rog să mă scuzați! Plec și eu acum."
        tu "Dar din întâmplare, știți cumva unde trebuie să merg? Că nu am mai fost până acum."
        bus " Din câte am văzut la ceilalți, o luați înainte, după la stânga și prin pădure."
        tu "Am înțeles, mulțumesc frumos!"
        tu "O zi bună!!"
        bus "Mulțumesc, la fel!"

        scene padure with fade
        "Dacă mă gândesc bine, ar fi putut să îmi dea niște coordonate false, doar să râdă de mine."
        "Dar voi merge pe mâna lui de data asta."

        scene intrare
        "După 30 minute de mers, ajung în fața unei tabere, nu știu sigur dacă e a mea sau nu."


        jump tabara

    return


    label tabara:
        ##INTRAREA IN TABARA

        "Acum am rămas aici singur și nu știu ce sa mai fac."

        "Așa că am hotărât să caut să vorbesc cu cineva, ca să nu rămân pe timpul nopții singur în sălbăticie."
        play music "audio/Afternoon.mp3" fadein 1.0
        scene tabara
        "Cum intru pe porțile taberei, îmi ies în cale niște cabane micuțe, roșii."
        "Vazându-le, stăteam să mă gândeam:"



    menu:




         "Dacă să aștept să văd dacă iese careva dintr-o căbănuță.":
            jump cabanute

         "Dacă să mă duc direct la un adult, care avea grijă de tabără.":
            jump adult

    return




    label adult:

        "Așa că am ales să mă duc direct la un porfesor sau ceva de genul ăsta."
        "El sigur poate să ma ajute cu problema mea."

        scene black
        "Umblând eu pe acolo, încercând să găsesc un adult, zăresc unul chiar în fața unui loc pentru făcut foc de tabără."
        "Așa că aleg să mă îndrept spre el."
        scene foc
        tu "Scuza-ți-mă, cumva sunteți profesorul care coordonează această tabără?"
        show noah_neutral with dissolve

        e "Da, eu sunt. Cu cine am ocazia sa vorbesc?"

        tu "Mă numesc [nume]. Am ajuns aici din greșeală."
        tu "Și aș vrea să vă întreb ceva."
        show noah_smile
        e "Spune. Cu ce vrei sa te ajut?"

        tu "Aș avea cum să rămân și eu aici. Nu am cum să mă întorc acasă."
        tu "Iar din câte am înțeles,  astăzi a fost ultima zi în care mai circulă autocarele."
        scene foc_blur
        "Nu am nicio idee daca e așa."
        "Tot ce știu este că nu mai am cum să plec de aici."
        scene foc
        show noah_sad
        tu "Vă rog mult, nu o să deranjez cu nimic."
        show noah_smile
        e "Dacă tot nu ai cum să pleci, am să fac o excepție și am să te las să rămâi la noi în tabără."

        tu "Mulțumesc, mulțumesc. O să am grijă ce fac pe aici."

        scene black
        play music ["audio/Daylight.mp3"] fadein 1.0 fadeout 1.0
        "După ce am reușit să răman până la urmă, profesorul a vrut să îmi arate cum să mă descurc aici."
        "M-a plimbat prin toată tabăra ca să îmi arete diferite locații."
        scene tabara
        "Spre exemplu căbănuțele pe care le-am văzut la început, care sunt pentru copii veniti aici."
        "Și spre final ajungem la cantină."
        scene cantina
        "Cum am ajuns acolo, stomacul meu nu a mai rezistat."
        scene cantina with vpunch
        tu "*GRRAWL"
        show noah_smile

        e "Se pare că nu mai reziști, așa ca o sa te las sa te duci să îți iei ceva de mancare."
        e "Oricum nu mai am ce să îți arăt."
        tu "Mulțumesc de tur, și pentru ca mi-ați permis să rămân aici."
        e "Nicio problemă, ne mai vedem."

        scene black
        play music ["audio/AhEhIOhYou.mp3"] fadein 1.0 fadeout 1.0
        "Cum mă uitam eu la profesor cum pleacă, încep să ma uit puțin prin jur."

        "Și încep să îmi dau seama de ceva."
        "Tabăra aceasta este plină toată de fete de vârsta mea."
        "Am fost atât de preocupat de faptul că am ajuns în tabăra greșită și la turul profesorului încât nu am vauzt asta."
        "Unii ar spune că e raiul pe pămant, și că numai în vise se poate întampla asta."
        "(Unul din aceștia fiind chiar eu)"
        "Dar cu cât stau și mă gandesc mai bine, cu atât cred că o să am o viață grea aici."
        "Nu cred eu că o să mă înțeleg eu cu fetele de aici."
        "Un băiat într-o tabără de fete."
        "IM-PO-SI-BIL"
        play music ["audio/Afternoon.mp3"] fadeout 1.0 fadein 1.0
        scene cantina
        "Cum stăteam și eram pierdut în gandurile mele, o fată hotărăște să ma deranjeze."

        jump roxana



    return

    label cabanute:
        $alegere = 1;
        "Așa că am ales să mă plimb prin jurul lor, poate așa am să gasesc si eu pe cineva."
        "După vreo 10 minute, dintr-una din căsuțe apare o fată."
        "Așa că am ales să o abordez."
        tu "Hei, bună."
        show sumi frown with dissolve
        nec "Bună.?."
        nec "Ce cauți tu aici?"
        tu "Am ajuns în tabăra greșită și vroiam să vad dacă pot să rămân și eu peste noapte."
        show sumi open with dissolve
        nec "Nu știu ce să spun, abia ne-am cunoscut."
        show sumi frown
        nec "Apropo, cum te numești, eu sunt [v]."
        tu "Eu sunt [nume], încântat de cunoștință."
        show sumi smile
        v "Păi dacă nu ai ce să faci, hai să mergem să mai vorbim cu niște prietene de ale mele."
        v "Poate au ele vreo idee."
        tu "Bine atunci, după tine."

        scene black
        "Mă țin eu dupa [v], care încearcă să își găsească prietenele."
        "Eu sper doar că am să rezolv cu problema rămasului peste noapte."
        scene cantina
        "Ajungem să trecem prin fața cantinei, când deodată stomacul meu nu poate rezista mirosului care vine din acea parte."
        scene cantina with vpunch
        tu "*GRRAWL"
        show sumi open blush with dissolve
        "Auzindu-mă [v], aceasta se înroșește la față."
        show sumi smile
        v "Hehe. Se pare că cuiva i s-a făcut foame."
        tu "Nu pot să neg asta, am fost pe drum toată ziua fără să mănânc nimic."
        v "Așteaptă aici și îți aduc eu ceva de la cantină."

        scene black
        play music "audio/AhEhIOhYou.mp3"
        "Cât timp stau și o aștept eu pe [v], am început să ma uit prin jur."
        "Și observ un lucru de care nu am bagat de seama."
        "Tabăra aceasta este plină toată de fete de vârsta mea."
        "Am fost atât de preocupat de faptul că am ajuns în tabăra greșită încât nu am vauzt asta."
        "Unii ar spune că e raiul pe pămant, și că numai în vise se poate întampla asta."
        "(Unul din aceștia fiind chiar eu)"
        "Dar cu cât stau și mă gandesc mai bine, cu atât cred că am să dorm eu în padure."
        "Nu are cum să mă lase să răman aici."
        "IM-PO-SI-BIL"
        play music ["audio/Afternoon.mp3"] fadeout 1.0 fadein 1.0
        "Între timp, [v] se întoarce de la cantina, cu ceva ce ar părea a fii pireu."

        scene cantina
        show sumi smile
        v "Hei, [nume]. Hai să stăm undeva să mâncăm, până nu se răcește."
        tu "Ok."
        "Ne asezăm noi pe o bancă, sub un copac,lângă căsuțele cele roșii ,și începem să mâncăm din pireul adus de ea."
        scene tabara
        "Cât timp mâncam, am început să vorbesc din ce în ce mai mult cu [v], de parcă ne știam de la grădiniță."
        "Ba cum am ajuns aici, ba ce am facut săptămâna trecută, conversația nu avela loc de sfârșit."
        "Până când, dintr-o dată apare o fată pe care nu am zărit-o când am intrat aici."
        jump roxana

    return
    label roxana:
        "Aceasta își îndreaptă degetul către mine și întreabă."
        play music ["audio/Out of the Loop.mp3"]
        show miu pout1 with dissolve

        nec "Cine ești tu și ce cauți aici?!?"
        tu "Mă numesc [nume]."
        tu "Iar în legătură cu ce caut aici, este o poveste lungă."
        nec "Nu îmi pasă mie asta."
        nec "Am să mă duc să te reclam la profesor."
        if alegere==0:
            #"Aici e labelul prof."
            tu "Deja am vorbit cu un profesor, și am hotărât că am să rămân aici."
            f1 "Nu se poate așa ceva."
            f1 "Mă duc imediat să îl aduc aici."

            scene black

            "Și în dată fata necunoscută pleacă în căutarea [e]."
            "Iar după puțin timp reușește și să îl găsească."
            scene cantina
            show noah_angry at right
            show miu pout1 at left
            e "Care e problema [f1]?"
            e "Ce neregulă tot vrei să îmi arăți??"
            f1 "Uitați aici. Această persoană nu are ce cauta aici!!"
            show noah_neutral at right
            e "Eu nu văd nicio problemă."
            e "Deja am vorbit cu [nume] și am hotărât ca să rămână la noi în tabără."
            hide miu pout1
            show rsz_3miu_sad at left

            f1 "Dar..."
            show noah_vangry at right with vpunch
            e "Niciun dar, să nu te mai aud cum te cerți."
            e "Că altfel zbori de aici!"
            f1 "Am inteles......."
            scene black
            "Și astfel am ajuns să mă întâlnesc eu cu [f1]."
            "Ce mai primă impresie..."
            scene cantina
            show noah_smile
            e "Nu băga de seamă ce s-a întâmplat. [f1] mereu e așa cu fețele noi."
            tu "Nicio problemă, o înțeleg."
            tu "Și eu aș reacționa așa dacă aș fii în locul ei."
            e "Dacă totul este bine, ok."
            play music ["audio/Afternoon.mp3"] fadeout 1.0 fadein 1.0
            e "Acum vino cu mine să ți-o prezint pe noua ta colega de cameră."
            scene black

            "Când am auzit ce a spus, m-am rușinat."
            "Eram sigur că o să mă cert cu cineva, dar nici nu mă gândeam că am să împart o cameră cu o altă fată."
            "Dacă o să fie cum a fost cu [f1], ce mă fac?"
            scene tabara
            "Ajungem noi la căbănuțele cele roșii pe care le-am mai vazut și ne oprim ăn fața uneia dintre ele."
            show noah_smile
            e "Aici o să fie camera ta."
            e "Iar aceasta o să fie colega ta de camera, [v]."
            e "[v], vino să îți vezi colegul!"

            "Cum se deschide ușa, apare o fată scundă, care părea să fie puțin rușinată."
            show sumi open small at right


            v "Bună, ma numesc [v], încântată de cunoștiință."
            tu "Bună, eu mă numesc [nume], de asemenea."
            e "Dacă totul este în regulă, eu am să mă întorc la treaba mea."
            scene black
            "Și astfel [e] pleacă, lasându-mă singur cu [v]."

            "Intrăm înauntru și începem să discutăm puțin câte puțin, astfel să ne cunoaștem mai bine."
            "Și spre surprinderea mea, [v] este o fata chiar drăguță."
            "Cu care am aflat că am multe lucruri în comun."
            "Astfel reușind să vorbim până dimineață."
            "Mă simțeam că o cunosc pe [v] de când eram la gradiniță."
            "Astfel reușind să îmi fac și prima prietenă aici."

            jump a_doua_zi

        if alegere==1:
            #"Aici e labelul fata."
            hide miu pout1
            "[v] văzându-mă, nu ezită să sară de partea mea."
            show miu pout1 at left with dissolve
            show sumi frown at right with dissolve

            v "[f1] lasăl pe [nume] în pace."
            v "Cu ce ți-a greșit!?"
            f1 "Cum poți să îi iei apărarea unui baiat!?"
            v "Și ce dacă!?"
            v "Mi se pare un băiat chiar ok, și nu vad nicio problemă dacă ar rămâne aici."
            scene black
            "Cât timp fetele se ceartă, am înțeles că numele fetei care nu mă suportă este [f1]."
            "Ar părea că ele două nu se înțeleg așa bine."
            "Dat fiind și personalitățile lor diferite."
            scene tabara
            "În timp ce fetele se certau, un profesor observă și alege să le despartă."
            e "HEEEEI, CE SE ÎNTÂMPLĂ AICI!!??!?"


            show rsz_3miu_sad at left
            show sumi frown at right
            with vpunch
            "Și îndată cele două se opresc."
            "După care [e] își aruncă privirea spre mine."
            hide rsz_3miu_sad
            hide sumi frown
            show noah_angry with dissolve
            e "Scuză-mă că te întreb, da' cine ești tu?"
            tu "Bună-ziua, ma numesc [nume]. Am ajuns aici din greșeală și nu m-ai am cum să plec."
            tu "Aș avea cum să răman aici? Promit că nu o să fac niciun rău."
            "La care [v] adaugă."
            show sumi open small at right
            v "Vă rog mult, promit că am să am eu grjă să nu se întâmple nimic."
            vtu "Vă rooooooog!!!"
            scene  black
            "Profesorul stă puțin pe gânduri, dar spre mirarea lui [f1], acesta acceptă să mă lase să rămân."
            scene tabara
            show noah_smile
            e "Hai că te las, atâta timp cât [v] o să stea cu ochii pe tine."
            v "Nu vă faceți griji, o să am mare grijă să nu se întâmple nimic."
            f1 "Nu e corect!!"
            "După care [f1] hotărăște să plece, spunandu-mi în timp ce trece pe lângă mine:"
            f1 "Nu ai să scapi așa ușor."
            hide noah_smile
            "După care eu cu [v] hotărâm să intrăm în cabanuță să ne culcam."
            play music ["audio/Afternoon.mp3"] fadeout 1.0 fadein 1.0
            jump a_doua_zi


    return

    label a_doua_zi:
        #AICI INCEPE A DOUA ZI
        scene tabara with fade
        "Mă trezesc eu dimineață, sculat fiind de sunetul naturii..."
        "Iau mă spăl pe dinți, îmi fac un duș, și o aștept pe [v] ca să mergem la cantină."
        tu "Ești gata, [v]?"
        show sumi smile
        v "Da, hai să mergem."
        scene black
        "Ne îndreptăm noi spre cantină."
        "Ajuns în fața acesteia începe să îmi tremure picioarele."
        "Ce o să spună ceilalți? Dacă o sa mă trateze cum m-a tratat [f1]?"
        "Ce mă fac??!?"
        scene cantina
        show sumi smile
        v "Hai, ce mai aștepți?"
        v "Nu intrăm?"
        tu "M-ai lasăma 2 minute să îmi adun puterile."
        show sumi open blush with dissolve


        "Atunci [v] mă apucă de braț și intră împreună cu mine pe ușă."
        scene black
        "Toată lumea se uita la noi, dar spre surprinderea mea, nimeni nu a avut aceeași reacție ca [f1]."
        "Ba chiar mai bine, multe dintre ele erau prietene cu [v], și au venit să se prezinte fiecare pe rând."
        "Mă simțeam ciudat. E prima dată când mi se întâmplă așa ceva."
        "După toate introducerile, lu-am și ne punem la masă să mâncăm, după care ieșim afară."
        scene cantina

        show sumi smile
        v "Ai văzut că nu a fost așa rau?"
        v "Ți-am spus eu că o să te înțelegi cu toată lumea."
        scene black
        "Ei bine, aproape toată lumea."
        "După ce s-a întâmplat ce s-a întâmplat ieri cu [f1], nu am mai dat de ea."
        "Poate plănuiește ceva."
        "Sper doar să nu fie prea umilitor."
        scene cantina
        show sumi open
        v "Ce ar fi dacă am face un foc de tabără, cu ocazia venirii tale în tabără?"
        tu "Ar suna chiar bine."
        tu "Eu ma bag."
        v "Atunci hai să ne apucăm să strângem exact ce ne trebuie."
        v "Lemne, carbuni, carne, etc."
        tu "Am înțeles, am să mă duc să fac rost de carne, iar tu poti sa vorbesti cu profesoru."
        tu "Poate ai cum să faci rost de lemne și cărbuni de la el."
        show sumi smile
        v "Ok, am să mă duc să îl caut pe profesor."
        tu "Atunci eu o să mă duc la cantină să vad ce fac în legătură cu carnea."

        scene black
        "Am intrat la cantină și l-am întrebat pe bucătar daca are cum să îmi dea niște carne ca să putem să o facem la focul de tabără."
        "Surprins plăcut, bucătarul reușește să ne dea carnea de care avem nevoie."
        play music "audio/Stride.mp3"
        "Mă îndrept eu către focul de tabără, unde mă întâlnesc cu [f1]."
        scene foc
        show miu pout1
        f1 "Se pare că ne întâlnim din nou."
        tu "[f1] cu ce ocazie ne onorezi această vizită??"
        f1 "Am auzit ca faceți o petrecere la focul de tabără, și vroiam să mă asigur că nu o să se întâmple nimic rau."
        tu "Dacă zici tu, bine."
        tu "Dar să nu te prind ca încerci vreo scamatorie. Și să distrugi totul."
        f1 "Nu.nu. Nu aș face eu așa ceva."
        f1 "Ai încredere în mine."
        tu "Ok, bine."
        tu "Atunci te aștept diseară."
        f1 "Voi fii garantat."


        scene black
        "Aleg să nu îmi complic mai mult viața încercând să îmi dau seama exact ce plan are [f1]."
        "Sper doar că o să fie totul în regulă."

        scene focnoapte


        "Am terminat până la urmă cu pregătirile, chiar când să se întunece."
        if muzica == 1:
            play music ["audio/Life Is Life.mp3"] fadein 1.0 fadeout 1.0

        else:
            play music ["audio/Formatia Alb si Negru (Laurentiu Popa) - Un trandafir creste la firida mea ( Machedoneasca ).mp3"] fadein 1.0 fadeout 1.0

        "Așa că am început să dam drumul la foc, si să îi dăm drumul la petrecere."
        "Toată lumea dansează și se distrează"
        "Până și profesorul se simte bine."
        scene black with vpunch

        "Cum stau și ma holbez la foc, cineva vine și îmi astupă ochii."
        tu "Hei, hei. Cine face asta?"
        nec "Ghici!"
        "După voce ar părea să fie [f1]."
        "Oare ea e, sau e [v]?"
        menu:


            "Să fie [f1]?":
                jump rox

            "Să fie [v]?":
                jump mar

        return

        label rox:
            tu "[f1], tu ești?"
            nec "Ai ghicit!!"
            scene focnoapte
            tu "Ce e cu toate astea, nu înteleg nimic."
            show rsz_1miu_catsmile
            f1 "Nu îți fă griji, a fost doar o glumă mică"
            show foc_blur
            "Să nu credeți că eram furios, eram doar surprins."
            "Mă așteptam la așa ceva de la [v], dar de la [f1] nici pe departe."
            "Și dacă stau să ma uit mai bine, [f1] arată destul de drăguț. Nu pot nega asta."
            scene focnoapte
            show rsz_1miu_catsmile

            tu "Chiar m-ai surprins."
            tu "Încep să cred că nu ești ceea ce păreai la început."
            show rsz_1miu_surprised
            f1 "Vorbești serios?"
            tu "Da, foarte."
            scene black
            "În momentul acela mi-am dat seama exact ce am facut, și rușinat fiind, mi-am acoperit fata cu palmele."
            "Ce o să creadă [f1] despre mine?"
            scene focnoapte
            show rsz_1miu_surprised
            f1 "Vreau să îmi cer scuze pentru cum m-am purtat."
            f1 "Ai putea să mă ierți??"
            tu "Scuze acceptate."
            tu "Nu pot să stau suparat pe o persoana asa draguță ca tine."
            scene foc_blur
            "De atunci am început să vorbesc din ce în ce mai mult cu [f1], și să o cunosc mult mai mult."
            "Așa că poate când ne-om revedea înafara taberei, sper să pot să o invit în oraș."

            return

            label mar:
                tu "[v], tu ești??"
                nec "Ai ghicit!!!"
                scene focnoapte
                show sumi  open blush
                tu "Ce e cu toate astea, nu înteleg nimic."
                v "Nu trebuie să întelegi nimic. Totul este în ordine."
                tu "Nu mă gândeam că vei face una ca asta."
                scene foc_blur
                "Sincer să fiu, nu am fost supărat în acel moment. Ba chiar am fost surprins."
                "Nu credeam ca [v] poate fii în stare de asta."
                "Ceea ce mă face să mă simt din ce în ce mai atras de ea."
                scene focnoapte
                show sumi open blush
                v "Sper că nu te simți ciudat acum."
                v "Dacă stau să mă gandesc mai bine, nu cred că trebuia să fac asta."
                tu "Stai... Nu trebuie să te simți prost."
                tu "Înteleg cum te simți."
                v "Deci.... Vrei să...."
                tu "Da... Vreau."
                scene black
                "Iar după ce s-a terminat tabăra, am început sa ieșim împreună."
                "Și încă am rămas îmăpreună."



                return







    return
