<script lang="ts">
    import Logo from "../Components/main/Logo.svelte";
    import Navbar from "../Components/NavBar/Main.svelte"
</script>
<div class="min-h-screen pb-5 w-full bg-[url('/CSSIMAGES/LoginBackground.webp')] bg-cover bg-center bg-no-repeat">
    <Navbar/>
    <Logo/>
    <div class="max-w-5xl mx-auto">
        <h2 class="text-5xl text-white my-15">Porque Um gerenciador de dnd</h2>
        <p class="text-white text-justify text-lg ms-10">
            A criação desse projeto foi para ajudar o gerenciamento dos recursos narrativos,mecânicos e visuais para sua mesa de D&D.
            Incialmente procurei outros sitemas para poder gerenciar melhor os recursos da minha campanha tanto pela pespectiva de jogador quanto pela do mestre,
            No entanto, todos os sistes ou eram pagos ou eram limitados e bastante instáveis. Diante dessa necessidade e uma revolta em transformarem isso em algo pago,
            meu amor a RPG's me fez querer facilitar para todos os metres e jogadores que quiserem usar esse site para facilitar e organizar anotações, imagens, personagens,
            NPC's e a própia party de forma mais simples, eficiente e didática.
        </p>
        <h2 class="text-5xl text-white my-15">Quem sou eu?</h2>
        <p class="text-white text-justify text-lg ms-10">
            Meu nome é João Gabriel Pereira Lopes, sou um programador Fullstack que quer se tornar um analista/cientista de dados,
            sou formado como técnico de informática no Colégio Pedro II. Atualmente tenho conhecimentos em python,javascritpt,svelte e react.
            Esse projeto é também uma aplicação daquilo que aprendi em meu curso, conceitos de programação reativa, restAPI e Banco de dados SQL Postgree.
        </p>
        <h2 class="text-5xl text-white my-15">Minha paixão por RPG's</h2>
        <p class="text-white text-justify text-lg ms-10">
            No ano de 2025 eu conheci RPG's por um sistema de demon slayer, totalmente desbalanceado e completamente quebrado.
            Meu primeiro personagem foi super sem graça e basicamente uma cópia do tanjiro, com as habilidades da resp do trovão. Depois do meu mestre abandonar essa campanha
            para focar em um sistema mais equilibrado sobre Jujutsu Kaisen. Assim, vendo o sistema de kimetsu morrer, eu quis manter ele vivo e me tornei mestre. 
            Rapidamente a campanha morreu por causa do sistema extremamente desequilibrado, porém, depois de um tempo o sistema de demon slayer foi substituido por D&D 5e, onde, 
            finalmente os jogadores ficaram animados e empolgados com a campanha.
        </p>
    </div>
</div>