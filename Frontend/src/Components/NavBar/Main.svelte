<script lang="ts">
    import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
    import { faHouse, faHatWizard,faPerson,faPeopleGroup, faCircleUser, faBook} from '@fortawesome/free-solid-svg-icons';
    import { onMount } from 'svelte';

    let width = 0;

    function handleResize() {
        width = window.innerWidth;
    }

    onMount(() => {
        handleResize();
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    });

</script>
<div class="flex flex-row bg-red-950 py-5 px-20 text-white items-center justify-between">
    <div class="text-3xl cursor-text {width < 768 ? 'flex-1/2' : 'flex-1/3'}">
        <label class="w-max cursor-pointer">
            <FontAwesomeIcon icon={faCircleUser} class="text-white me-4"/>
        {#if width > 1000}
            Login
        {/if}        
        </label>
    </div>
        
    {#if width > 750}
        <ul class="flex flex-row decoration-none gap-20  {width < 768 ? 'flex-1/2' : 'flex-1/3'} justify-center">
            <li class="flex flex-row items-center text-3xl">
                <a href="/">
                    <FontAwesomeIcon icon={faHouse} class="text-white cursor-pointer"/>
                </a>
            </li>
            <li class="flex flex-row items-center text-3xl">
                <FontAwesomeIcon icon={faHatWizard} class="text-white cursor-pointer"/>
            </li>
            <li class="flex flex-row items-center text-3xl">
                <FontAwesomeIcon icon={faPerson} class="text-white cursor-pointer"/>
            </li>
            <li class="flex flex-row items-center text-3xl">
                <FontAwesomeIcon icon={faPeopleGroup} class="text-white cursor-pointer"/>
            </li>
            <li class="flex flex-row items-center text-3xl">
                <FontAwesomeIcon icon={faBook} class="text-white cursor-pointer"/>
            </li>
        </ul>
    {:else}
    {/if}        
    {#if width > 900}
        <div class="flex flex-1/3 justify-end items-center">
            D&D<img src="/dndLogo.png" alt="" class="h-10 ms-5">
        </div>
    {/if}
</div>