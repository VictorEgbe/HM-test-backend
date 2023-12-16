
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Sector, SectorHeading, User
from .serializers import CreateSectorSerializer, EditSerializer


@api_view(http_method_names=('GET', 'POST'))
def index(request):

    if request.method == 'GET':
        sector_headings = SectorHeading.objects.all()
        data = []
        for heading in sector_headings:
            data.append(
                {
                    "id": heading.pk,
                    "name": heading.name,
                    "sectors": [{"id": s.pk, "name": s.name} for s in heading.sector_set.all()]
                }
            )

        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CreateSectorSerializer(data=request.data)
        if serializer.is_valid():
            sector_list = serializer.data.get('sectors')
            agree = serializer.data.get('agree')
            user_name = serializer.data.get('user_name')
            user = User.objects.create(name=user_name, agreed=agree)
            for sector_name in sector_list:
                db_sector = Sector.objects.get(name=sector_name)
                user.sectors.add(db_sector)
            user.save()

            return Response({'userName': user.name}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=('GET', 'PUT'))
def user_sectors(request, username):
    user = User.objects.get(name=username)
    if request.method == 'GET':
        sectors = user.sectors.all()
        headings_names = list(set([s.heading.name for s in sectors]))
        data = []
        for h_name in headings_names:
            heading = SectorHeading.objects.get(name=h_name)
            data.append(
                {
                    "id": heading.pk,
                    "name": heading.name,
                    "sectors": [{"id": s.pk, "name": s.name} for s in sectors.filter(heading__name=heading.name)]
                }
            )

        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = EditSerializer(data=request.data)
        if serializer.is_valid():
            new_username = serializer.data.get('user_name')
            sectors = serializer.data.get('sectors')
            user.name = new_username
            user.sectors.clear()

            for sector_name in sectors:
                db_sector = Sector.objects.get(name=sector_name)
                user.sectors.add(db_sector)

            user.save()

            return Response({'userName': user.name}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
