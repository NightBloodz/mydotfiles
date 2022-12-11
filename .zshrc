# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

typeset -g POWERLEVEL9K_INSTANT_PROMPT=off
# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=5000
SAVEHIST=100000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall

autoload -Uz compinit
compinit
# End of lines added by compinstall

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/dirhistory/dirhistory.plugin.zsh
source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh/plugins/sudo/sudo.plugin.zsh
source /usr/share/zsh/plugins/extract/extract.plugin.zsh
source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh
source /usr/share/zsh/plugins/sudo/sudo.plugin.zsh
source /usr/share/zsh/plugins/arch/archlinux.plugin.zsh

alias h='history'
alias ls='lsd'
alias cat='bat'
alias cat2='/bin/cat'
alias icat="kitty +kitten icat"
alias aslr_off='echo 0 | sudo tee /proc/sys/kernel/randomize_va_space'
alias aslr_on='echo 1 | sudo tee /proc/sys/kernel/randomize_va_space'
alias l='ls -l'
alias ll='ls -al'
alias xclip='/usr/bin/xclip -selection clipboard'


bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down


# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh


bindkey "^[[H" beginning-of-line
bindkey "^[[F" end-of-line
bindkey "^[[3~" delete-char

bindkey "^[[1;2C" forward-word
bindkey "^[[1;2D" backward-word

bindkey "^[[1;7D" select-a-word
bindkey "^[[1;7C" select-a-word

#variables
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:~/.local/bin:/usr/local/sbin:/sbin:/usr/sbin:/snap/bin




export hip=$(ip a | grep "tun0" | grep "inet" | awk '{print $2}' | sed 's/\/23//g') 
chip(){
  echo $hip | xclip -selection clipboard
}

tip () {
   export tip=$1

}



mkt () {
  mkdir {ports,files,scripts}
}



neofetch


POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true
source /usr/share/zsh-theme-powerlevel10k/powerlevel.zsh-theme
