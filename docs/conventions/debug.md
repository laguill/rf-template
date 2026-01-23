# Guide : Tests avec Chrome Debug

## Utilisation quotidienne

1. **Lancez** `uv run just start-chrome-debug`
2. Chrome s'ouvre → **Naviguez manuellement** vers la page à tester
3. **Connectez-vous** si nécessaire
4. **Lancez votre test** : `robot mon_test.robot`
5. Le test s'exécute sur la page déjà ouverte ✅
6. Chrome **reste ouvert** après le test
7. Modifiez votre test et **relancez** → ultra rapide !

```robotframework title="tests_debug/debug_login.robot"
--8<-- "tests_debug/debug_login.robot"

```
