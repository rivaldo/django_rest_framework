from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from rest_framework import viewsets, generics
from escola.serializers import ListaMatriculasEstudanteSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculasEstudante(generics.ListAPIView):
    serializer_class = ListaMatriculasEstudanteSerializer
    
    def get_queryset(self):
        estudante = self.kwargs['pk']
        return Matricula.objects.filter(estudante=estudante)
    
class ListaMatriculaCurso(generics.ListAPIView):
    serializer_class = ListaMatriculasEstudanteSerializer
    
    def get_queryset(self):
        curso = self.kwargs['pk']
        return Matricula.objects.filter(curso=curso)
#