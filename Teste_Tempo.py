import cProfile
import pstats
import caixeiroViajante

# Salvar resultados no formato binário esperado
profiler = cProfile.Profile()
profiler.enable()
caixeiroViajante.testes()  # Substitua pela função que você quer analisar
profiler.disable()

# Salvar os dados do perfil em um arquivo binário
profiler.dump_stats("resultados.prof")

# Analisar o arquivo com pstats
stats = pstats.Stats("resultados.prof")
stats.strip_dirs().sort_stats("time").print_stats(10)
