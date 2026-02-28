<script lang="ts">
    import Navbar from "../../Components/NavBar/Main.svelte"
</script>
<div class="min-h-screen w-full bg-[#0c0c0c] flex flex-col">
    <Navbar/>
    <form 
    class="flex-1 bg-[url('/CSSIMAGES/MainBackground.jpg')] bg-cover bg-center bg-no-repeat relative" action="POST">
        <div 
        class="md:max-w-md bg-[#ffffff9f] md:h-9/12 absolute left-1/2 top-1/2 translate-x-[-50%] translate-y-[-50%] md:rounded-4xl bg-blur-md scale-105 flex-col flex h-[calc(100%-40px)] w-[calc(100%-20px)] px-5 md:px-15 md:py-3 justify-between">
            <div 
            class="w-full h-max flex flex-1 flex-col gap-3">
                <label for="nickname" class="text-2xl text-red-900">Nickname</label>
                <input type="text" name="nickname" placeholder="Seu nickname" class="p-5 rounded-full w-full">
            </div>
            <div class="w-full h-max flex flex-1 flex-col gap-3">
                <label for="Email" class="text-2xl text-red-900">Email</label>
                <input type="email" name="Email" placeholder="Seu Email" class="p-5 rounded-full w-full">
            </div>
            <div class="w-full h-max flex flex-1 flex-col gap-3">
                <label for="password" class="text-2xl text-red-900">Password</label>
                <input type="password" name="password" placeholder="Seu password" class="p-5 rounded-full w-full">
            </div>
            <div class="w-full h-max flex flex-1 flex-col gap-3">
                <label for="PasswordConfirm" class="text-2xl text-red-900">Password Confirm</label>
                <input type="password" name="PasswordConfirm" placeholder="Seu Password Confirm" class="p-5 rounded-full w-full">
            </div>
            <button 
            class="bg-blue-900 p-4 rounded-full text-white text-4xl flex flex-row items-center justify-center">
                SUBMIT
            </button>
        </div>
    </form>
</div>